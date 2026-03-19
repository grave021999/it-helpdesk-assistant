# 🤖 IT Helpdesk Assistant

An AI-powered IT Helpdesk Assistant built with **Streamlit**, featuring an **A2A (Agent-to-Agent) orchestration layer** and **MCP (Model Context Protocol)** integration for intelligent IT ticket querying and support.

---

## ✨ Features

- **Conversational Chat Interface** — Natural language querying for IT tickets via Streamlit
- - **A2A Orchestration Layer** — Agent-to-Agent protocol for seamless task delegation
  - - **MCP Integration** — Model Context Protocol tools for structured ticket operations
    - - **Session Management** — Persistent chat history with easy reset functionality
      - - **Real-time Processing** — Instant AI-powered responses to helpdesk queries
       
        - ---

        ## 🏗️ Architecture

        ```
        ├── app.py                  # Streamlit entry point
        ├── src/
        │   ├── a2a_layer/          # Agent-to-Agent orchestration
        │   ├── config/             # Configuration settings
        │   ├── data_layer/         # Data access and management
        │   └── mcp_layer/          # MCP tool integrations
        ├── requirements.txt
        └── .gitignore
        ```

        ---

        ## 🚀 Getting Started

        ### Prerequisites

        - Python 3.9+
        - - pip
         
          - ### Installation
         
          - ```bash
            git clone https://github.com/grave021999/it-helpdesk-assistant.git
            cd it-helpdesk-assistant
            pip install -r requirements.txt
            ```

            ### Run the App

            ```bash
            streamlit run app.py
            ```

            ---

            ## 🛠️ Tech Stack

            | Technology | Purpose |
            |---|---|
            | Python | Core language |
            | Streamlit | Web UI framework |
            | A2A Protocol | Agent orchestration |
            | MCP | Model Context Protocol |

            ---

            ## 📝 Usage

            1. Launch the application with `streamlit run app.py`
            2. 2. Enter your query in the text input (e.g., "show weekly report" or "open tickets")
               3. 3. Click **Ask** to get AI-powered responses
                  4. 4. Use the sidebar to start a new chat session
                    
                     5. ---
                    
                     6. ## 📄 License
                    
                     7. This project is open source and available under the [MIT License](LICENSE).
