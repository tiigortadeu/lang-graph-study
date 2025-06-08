import streamlit as st
from chatbot import PersonalAssistantChatbot
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import os

# Configure Streamlit page
st.set_page_config(
    page_title="Personal Assistant Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stChat > div {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    
    .assistant-message {
        background-color: #f3e5f5;
        margin-right: 20%;
    }
    
    .tool-message {
        background-color: #e8f5e8;
        margin-right: 20%;
        font-size: 0.9em;
        opacity: 0.8;
    }
    
    .main-header {
        text-align: center;
        color: #1976d2;
        margin-bottom: 2rem;
    }
    
    .feature-box {
        padding: 1rem;
        border-left: 4px solid #1976d2;
        background-color: #f8f9fa;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .setup-box {
        padding: 1rem;
        border-left: 4px solid #ff9800;
        background-color: #fff3e0;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .success-box {
        padding: 1rem;
        border-left: 4px solid #4caf50;
        background-color: #e8f5e8;
        margin: 1rem 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<h1 class='main-header'>🤖 Personal Assistant Chatbot</h1>", unsafe_allow_html=True)
    
    # Sidebar for configuration and info
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check for API key
        api_key = st.text_input(
            "Google API Key", 
            type="password", 
            value=os.getenv("GOOGLE_API_KEY", ""),
            help="Enter your Google API key for Gemini AI"
        )
        
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
        
        st.markdown("---")
        
        # Gmail Setup Status
        st.header("📧 Gmail Setup")
        
        credentials_exists = os.path.exists("credentials.json")
        token_exists = os.path.exists("token.json")
        
        if credentials_exists:
            st.markdown("""
            <div class='success-box'>
            ✅ <strong>credentials.json found!</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='setup-box'>
            ⚠️ <strong>credentials.json missing!</strong><br>
            Please download it from Google Cloud Console.
            </div>
            """, unsafe_allow_html=True)
        
        if token_exists:
            st.markdown("""
            <div class='success-box'>
            ✅ <strong>Authentication token found!</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("🔑 You'll be prompted to authenticate on first use.")
        
        st.markdown("---")
        
        st.header("🛠️ Available Tools")
        
        # Show available tools after chatbot is initialized
        if "chatbot" in st.session_state:
            tools = st.session_state.chatbot.get_available_tools()
            if tools:
                st.markdown("""
                <div class='success-box'>
                <strong>Gmail Tools Active:</strong>
                </div>
                """, unsafe_allow_html=True)
                
                for tool in tools:
                    if "send" in tool.lower():
                        st.write("📤 Send Emails")
                    elif "draft" in tool.lower():
                        st.write("📝 Create Drafts")
                    elif "search" in tool.lower():
                        st.write("🔍 Search Emails")
                    elif "message" in tool.lower():
                        st.write("📨 Read Messages")
                    elif "thread" in tool.lower():
                        st.write("🧵 Get Threads")
            else:
                st.markdown("""
                <div class='setup-box'>
                ⚠️ <strong>No Gmail tools available</strong><br>
                Check your Gmail setup.
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.header("💬 Usage Examples")
        st.markdown("""
        <div class='feature-box'>
        <strong>📤 Send Emails:</strong><br>
        "Send an email to john@example.com with subject 'Meeting Tomorrow' and message 'Hi John, let's meet at 3 PM tomorrow.'"
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
        <strong>📝 Create Drafts:</strong><br>
        "Create a draft email to sarah@company.com about the project update"
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-box'>
        <strong>🔍 Search Emails:</strong><br>
        "Search for emails from john@example.com" or "Find emails with subject containing 'meeting'"
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "chatbot" not in st.session_state:
        if not api_key:
            st.error("⚠️ Please enter your Google API Key in the sidebar to get started!")
            st.stop()
        
        try:
            with st.spinner("Initializing chatbot and Gmail integration..."):
                st.session_state.chatbot = PersonalAssistantChatbot()
        except Exception as e:
            st.error(f"❌ Failed to initialize chatbot: {str(e)}")
            st.stop()
    
    # Display setup instructions if Gmail not properly configured
    if "chatbot" in st.session_state:
        tools = st.session_state.chatbot.get_available_tools()
        if not tools:
            st.warning("⚠️ Gmail tools are not available. The chatbot can still help with general tasks, but email functionality won't work.")
            
            with st.expander("📋 Gmail Setup Instructions", expanded=True):
                st.markdown("""
                **To enable Gmail functionality:**
                
                1. **Go to [Google Cloud Console](https://console.cloud.google.com/)**
                2. **Create a new project or select existing one**
                3. **Enable the Gmail API**
                4. **Create OAuth 2.0 credentials**
                5. **Download the credentials as `credentials.json`**
                6. **Place `credentials.json` in the same folder as this app**
                7. **Restart the application**
                
                **Required OAuth 2.0 Scopes:**
                - `https://mail.google.com/` (full Gmail access)
                
                **Note:** On first use, you'll be redirected to authenticate with Google.
                """)
    
    # Display chat messages
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            if isinstance(message, dict):
                msg_type = message["type"]
                content = message["content"]
                
                if msg_type == "user":
                    with st.chat_message("user"):
                        st.write(content)
                elif msg_type == "assistant":
                    with st.chat_message("assistant"):
                        st.write(content)
                elif msg_type == "tool":
                    with st.chat_message("assistant"):
                        st.info(f"🔧 Tool Result: {content}")
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat
        st.session_state.messages.append({"type": "user", "content": prompt})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get chatbot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response_messages = st.session_state.chatbot.chat(
                        prompt, 
                        st.session_state.chat_history
                    )
                    
                    # Update chat history with all messages
                    st.session_state.chat_history.extend(response_messages)
                    
                    # Display and store responses
                    for msg in response_messages:
                        if isinstance(msg, AIMessage):
                            content = msg.content
                            if content:  # Only show non-empty AI messages
                                st.write(content)
                                st.session_state.messages.append({
                                    "type": "assistant", 
                                    "content": content
                                })
                        elif isinstance(msg, ToolMessage):
                            st.info(f"🔧 Tool Result: {msg.content}")
                            st.session_state.messages.append({
                                "type": "tool", 
                                "content": msg.content
                            })
                    
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "type": "assistant", 
                        "content": error_msg
                    })

if __name__ == "__main__":
    main() 