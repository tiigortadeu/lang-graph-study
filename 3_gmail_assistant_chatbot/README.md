# Personal Assistant Chatbot 🤖

A powerful personal assistant chatbot built with LangGraph, Google Gemini AI 2.0, and full Gmail integration using the official LangChain Gmail Toolkit, all wrapped in a beautiful Streamlit interface.

## Features ✨

- **LangGraph Workflow**: Uses LangGraph to create a sophisticated conversation flow
- **Google Gemini AI 2.0**: Powered by the latest Gemini 2.0 Flash model
- **Full Gmail Integration**: Complete Gmail functionality with official LangChain toolkit
- **Multiple Gmail Tools**: Send emails, create drafts, search emails, read messages, and manage threads
- **Streamlit Interface**: Clean, modern web interface with real-time tool status
- **Tool Calling**: Seamless integration with Gmail API tools
- **Chat History**: Maintains conversation context
- **OAuth Authentication**: Secure Google authentication

## Gmail Tools Available 🛠️

1. **📤 GmailSendMessage** - Send emails directly
2. **📝 GmailCreateDraft** - Create email drafts
3. **🔍 GmailSearch** - Search through your emails
4. **📨 GmailGetMessage** - Read specific email messages
5. **🧵 GmailGetThread** - Get email conversation threads

## Setup Instructions 🚀

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key for later use

### 3. Gmail API Setup (Required)

**Step 1: Google Cloud Console Setup**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click "Enable"

**Step 2: Create OAuth 2.0 Credentials**

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. Choose "Desktop application" as application type
4. Give it a name (e.g., "Gmail Chatbot")
5. Download the credentials JSON file
6. Rename it to `credentials.json`
7. Place `credentials.json` in the same folder as your app files

**Step 3: Configure OAuth Consent Screen**

1. Go to "APIs & Services" > "OAuth consent screen"
2. Choose "External" user type
3. Fill in the required information:
   - App name: "Personal Assistant Chatbot"
   - User support email: Your email
   - Developer contact: Your email
4. Add scopes:
   - `https://mail.google.com/` (full Gmail access)
5. Add test users (your Gmail address)

### 4. Environment Variables

Create a `.env` file in the project directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

Or enter your API key directly in the Streamlit sidebar when running the app.

### 5. Run the Application

```bash
streamlit run app.py
```

**First Run Authentication:**
- The app will open in your browser at `http://localhost:8501`
- On first use, you'll be redirected to Google's OAuth consent screen
- Grant the necessary permissions
- You'll be redirected back to the app
- A `token.json` file will be created for future sessions

## Usage Examples 💬

### 📤 Sending Emails

"Send an email to john@example.com with subject 'Meeting Tomorrow' and message 'Hi John, let's meet at 3 PM tomorrow.'"

"Email sarah@company.com about the project update with subject 'Project Status' and tell her the project is on track."

### 📝 Creating Drafts

"Create a draft email to team@company.com about the quarterly review"

"Draft an email to client@business.com thanking them for their business"

### 🔍 Searching Emails

"Search for emails from john@example.com"

"Find emails with subject containing 'meeting'"

"Search for emails received last week"

### 📨 Reading Messages

"Show me the latest email from sarah@company.com"

"Get the email with subject 'Project Update'"

### 🧵 Managing Threads

"Get the email thread about the project discussion"

"Show me the conversation with john@example.com"

### 💬 General Assistance

- "What's the weather like today?"
- "Help me write a professional email"
- "Explain quantum computing in simple terms"

## Architecture 🏗️

The application uses a LangGraph workflow with the following components:

1. **Chatbot Node**: Main conversation handler powered by Gemini AI
2. **Tool Node**: Handles Gmail API tool executions
3. **State Management**: Maintains conversation history and context
4. **Conditional Routing**: Determines when to use tools vs. continue conversation
5. **Gmail Toolkit**: Official LangChain Gmail integration with full API access

## Files Structure 📁

```
3_test/
├── app.py              # Main Streamlit application
├── chatbot.py          # LangGraph chatbot implementation
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── credentials.json    # Gmail API credentials (you need to create this)
└── token.json         # Authentication token (created automatically)
```

## Troubleshooting 🔧

### Common Issues

1. **Gmail API Not Enabled**: Make sure Gmail API is enabled in Google Cloud Console
2. **Missing credentials.json**: Download OAuth 2.0 credentials from Google Cloud Console
3. **Authentication Errors**: Check OAuth consent screen configuration and test users
4. **Permission Denied**: Ensure your Gmail account is added as a test user
5. **Scope Issues**: Verify that `https://mail.google.com/` scope is included

### Setup Checklist ✅

- [ ] Google Cloud Project created
- [ ] Gmail API enabled
- [ ] OAuth 2.0 credentials created and downloaded
- [ ] `credentials.json` file in project folder
- [ ] OAuth consent screen configured
- [ ] Test users added (your Gmail address)
- [ ] Google API key obtained
- [ ] Dependencies installed

### Authentication Flow

1. First run: OAuth consent screen → Grant permissions → Return to app
2. Subsequent runs: Automatic authentication using saved token
3. Token refresh: Handled automatically by the toolkit

## Security Notes 🔒

- **credentials.json**: Contains sensitive OAuth credentials - never commit to version control
- **token.json**: Contains access tokens - never commit to version control
- **Scopes**: The app requests full Gmail access (`https://mail.google.com/`)
- **Local Storage**: Tokens are stored locally on your machine

## Customization 🎨

You can easily extend the chatbot by:

1. Adding more Gmail tools or custom tools in `chatbot.py`
2. Modifying the system prompt for different behavior
3. Adjusting the Streamlit interface in `app.py`
4. Adding new conversation nodes to the LangGraph workflow
5. Implementing additional Google Workspace APIs

## Requirements 📋

- Python 3.8+
- Google API Key (for Gemini AI)
- Google Cloud Project with Gmail API enabled
- OAuth 2.0 credentials (credentials.json)
- Gmail account for testing

## License 📄

This project is open source and available under the MIT License. 