import os
from typing import TypedDict, Annotated, List, Dict, Any
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

class PersonalAssistantChatbot:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.7
        )
        
        # Initialize Gmail toolkit with proper authentication
        self.gmail_toolkit = self._initialize_gmail_toolkit()
        
        if self.gmail_toolkit:
            # Get all available Gmail tools
            self.tools = self.gmail_toolkit.get_tools()
            st.success(f"✅ Gmail toolkit initialized with {len(self.tools)} tools!")
        else:
            st.error("❌ Failed to initialize Gmail toolkit. Please check your credentials.")
            self.tools = []
        
        # Bind tools to LLM
        if self.tools:
            self.llm_with_tools = self.llm.bind_tools(self.tools)
        else:
            self.llm_with_tools = self.llm
        
        # Build the graph
        self.graph = self._build_graph()
    
    def _initialize_gmail_toolkit(self):
        """Initialize Gmail toolkit with proper authentication and redirect URI"""
        try:
            # Get credentials with proper configuration for desktop app
            credentials = get_gmail_credentials(
                token_file="token.json",
                scopes=["https://mail.google.com/"],
                client_secrets_file="credentials.json",
            )
            
            # Build the API resource
            api_resource = build_resource_service(credentials=credentials)
            
            # Create the toolkit
            toolkit = GmailToolkit(api_resource=api_resource)
            
            return toolkit
            
        except FileNotFoundError:
            st.error("❌ credentials.json file not found. Please follow the setup instructions.")
            return None
        except Exception as e:
            error_msg = str(e)
            if "redirect_uri_mismatch" in error_msg.lower():
                st.error("❌ OAuth Redirect URI Error!")
                st.warning("🔧 **Quick Fix Required:**")
                st.info("1. Go to Google Cloud Console > APIs & Services > Credentials")
                st.info("2. Click on your OAuth 2.0 Client ID")
                st.info("3. In 'Authorized redirect URIs', add: `http://localhost:8080/`")
                st.info("4. Also add: `http://localhost`")
                st.info("5. Save and try again")
                st.info("6. Alternative: Download credentials again and select 'Desktop Application' type")
            else:
                st.error(f"❌ Failed to initialize Gmail toolkit: {error_msg}")
                st.info("📋 Make sure you have:")
                st.info("1. Downloaded credentials.json from Google Cloud Console")
                st.info("2. Selected 'Desktop Application' as application type")
                st.info("3. Enabled Gmail API in your Google Cloud project")
                st.info("4. Added your email as a test user in OAuth consent screen")
            return None
    
    def _build_graph(self):
        """Build the LangGraph workflow"""
        
        def chatbot_node(state: State):
            """Main chatbot node that processes user input"""
            system_prompt = """You are a helpful personal assistant with access to Gmail tools. You can:

1. **Send emails** - Use GmailSendMessage tool
2. **Create drafts** - Use GmailCreateDraft tool  
3. **Search emails** - Use GmailSearch tool
4. **Read emails** - Use GmailGetMessage tool
5. **Get email threads** - Use GmailGetThread tool

When a user asks you to send an email:
- Extract the recipient email address
- Create an appropriate subject line
- Compose the email content
- Use the GmailSendMessage tool

When a user asks to search emails:
- Use appropriate search terms
- Use the GmailSearch tool

Always be helpful, polite, and professional in your responses. If you're unsure about email addresses or content, ask for clarification."""

            response = self.llm_with_tools.invoke(
                [
                    ("system", system_prompt),
                    *state["messages"]
                ]
            )
            return {"messages": [response]}
        
        def tool_node(state: State):
            """Handle tool calls"""
            last_message = state["messages"][-1]
            
            if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
                return {"messages": []}
            
            tool_messages = []
            for tool_call in last_message.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
                # Find and execute the tool
                for tool in self.tools:
                    if tool.name == tool_name:
                        try:
                            result = tool.invoke(tool_args)
                            tool_messages.append(
                                ToolMessage(
                                    content=str(result),
                                    tool_call_id=tool_call["id"]
                                )
                            )
                        except Exception as e:
                            error_msg = f"Error executing {tool_name}: {str(e)}"
                            tool_messages.append(
                                ToolMessage(
                                    content=error_msg,
                                    tool_call_id=tool_call["id"]
                                )
                            )
                        break
                else:
                    # Tool not found
                    tool_messages.append(
                        ToolMessage(
                            content=f"Tool {tool_name} not found",
                            tool_call_id=tool_call["id"]
                        )
                    )
            
            return {"messages": tool_messages}
        
        def should_continue(state: State):
            """Determine if we should continue or end"""
            last_message = state["messages"][-1]
            if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
                return "tools"
            return END
        
        # Create the graph
        workflow = StateGraph(State)
        
        # Add nodes
        workflow.add_node("chatbot", chatbot_node)
        
        if self.tools:  # Only add tool node if we have tools
            workflow.add_node("tools", tool_node)
        
        # Set entry point
        workflow.set_entry_point("chatbot")
        
        # Add conditional edges
        if self.tools:
            workflow.add_conditional_edges(
                "chatbot",
                should_continue,
                {
                    "tools": "tools",
                    END: END
                }
            )
            # Add edge from tools back to chatbot
            workflow.add_edge("tools", "chatbot")
        else:
            # If no tools, just end after chatbot
            workflow.add_edge("chatbot", END)
        
        return workflow.compile()
    
    def chat(self, message: str, chat_history: List[BaseMessage] = None):
        """Process a chat message and return the response"""
        if chat_history is None:
            chat_history = []
        
        # Add the new user message
        messages = chat_history + [HumanMessage(content=message)]
        
        # Run the graph
        response = self.graph.invoke({"messages": messages})
        
        return response["messages"]
    
    def get_available_tools(self):
        """Get list of available tool names"""
        if not self.tools:
            return []
        return [tool.name for tool in self.tools] 