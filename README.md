🤖 Agentic Enterprise AI
ET Hackathon 2026 — Multi-Agent Autonomous Workflow System

A LangGraph-powered multi-agent system that takes ownership of complex enterprise processes end-to-end. Give it any unstructured input — meeting notes, process triggers, incident alerts — and 5 specialized AI agents handle the full lifecycle: extraction → planning → execution → monitoring → validation. With automatic self-correction, retry logic, and a full audit trail.

✨ Features
🔍 Extraction Agent — Parses raw text into structured tasks with owners, deadlines & priorities
📋 Planning Agent — Builds optimized execution plan respecting task dependencies
⚙️ Execution Agent — Executes tasks in priority order, simulates real enterprise actions
📡 Monitoring Agent — Tracks health score, detects delays, routes recovery in real-time
🔄 Recovery Agent — Self-corrects failures with LLM-guided retry; escalates at max retries
✅ Validation Agent — Final quality gate ensuring completeness + audit coverage
📜 Full Audit Trail — Every agent decision timestamped and logged
🌐 REST API — FastAPI backend with CORS, ready for UI integration
⚛️ React Dashboard — Real-time agent status, results, and workflow history
🏗️ Architecture
┌─────────────────────────────────────────────────────────────┐
│                    React Frontend (Vite)                     │
│                    http://localhost:5174                     │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP POST /api/workflows/run
┌──────────────────────────▼──────────────────────────────────┐
│                  FastAPI Backend (Uvicorn)                   │
│                    http://localhost:9000                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│               LangGraph State Machine                        │
│                                                             │
│  Extraction → Planning → Execution ←──────────┐            │
│                              │                │            │
│                          Monitoring           │            │
│                         /    |    \           │            │
│                    running  done  failed      │            │
│                       │      │       │        │            │
│                   (loop)  Validate  Recovery──┘            │
│                              │                             │
│                            END                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│              Gemini 2.5 Flash (Primary LLM)                 │
│         Auto-fallback → 2.0-flash → 2.0-flash-001          │
│              Exponential backoff on rate limits             │
└─────────────────────────────────────────────────────────────┘
🛠️ Tech Stack
Layer	Technology
Agent Orchestration	LangGraph 1.1
Backend API	FastAPI + Uvicorn
LLM	Google Gemini 2.5 Flash (REST)
Frontend	React 19 + Vite
Storage	JSON file store
Logging	structlog + Rich
Env Config	python-dotenv
🚀 Setup & Installation
Prerequisites
Python 3.11+
Node.js 18+
A Google Gemini API key (free at aistudio.google.com)
1. Clone the Repository
git clone https://github.com/your-username/agentic_enterprise_ai-ET-Hackathon.git
cd agentic_enterprise_ai-ET-Hackathon
2. Backend Setup
cd backend
Install Python dependencies:

pip install -r requirements.txt
Create your .env file:

cp .env.example .env
Edit .env and fill in your API key:

GOOGLE_API_KEY=your_gemini_api_key_here
CLOUD_LLM_MODEL=gemini-2.5-flash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=
API_HOST=0.0.0.0
API_PORT=9000
SIMULATE_FAILURE=false
FAILURE_RATE=0.3
💡 Get a free Gemini API key at aistudio.google.com/apikey

Start the backend server:

# Windows
set PYTHONUTF8=1
uvicorn main:app --reload --port 9000

# Mac / Linux
PYTHONUTF8=1 uvicorn main:app --reload --port 9000
Backend will be live at http://localhost:9000
Swagger docs at http://localhost:9000/docs

3. Frontend Setup
Open a new terminal:

cd frontend
npm install
npm run dev
Frontend will be live at http://localhost:5174

4. Verify Everything Works
# Test the backend health endpoint
curl http://localhost:9000/api/health

# Expected: {"status":"online","total_workflows":0,"last_run":null}
Or open http://localhost:5174 in your browser and run a workflow.

💡 Usage
Via the Web UI
Open http://localhost:5174
Paste any enterprise text into the input box:
Meeting Notes - Q2 Planning | April 2026

Alice to send roadmap to all stakeholders by April 5th. HIGH priority.
Bob to complete API integration for payment module by April 8th. HIGH priority.
Carol to deliver updated UI mockups by April 10th. MEDIUM priority.
Bob to schedule load testing with DevOps by April 15th. LOW priority.
Click Run Workflow
Watch agents process in real-time
View results: tasks, execution plan, audit log, health score
Via the API
curl -X POST http://localhost:9000/api/workflows/run \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Alice to send roadmap by April 5th. HIGH priority. Bob to finish API by April 8th. HIGH priority.",
    "simulate_failure": false
  }'
Enable failure simulation (demo mode — shows recovery agent in action):

curl -X POST http://localhost:9000/api/workflows/run \
  -H "Content-Type: application/json" \
  -d '{"input": "your input here", "simulate_failure": true}'
📡 API Endpoints
Method	Endpoint	Description
GET	/api/health	Health check + total workflow count
POST	/api/workflows/run	Trigger a new workflow
GET	/api/workflows	List all past workflow runs
GET	/api/workflows/{id}	Get a specific workflow by ID
DELETE	/api/workflows/clear	Clear all workflow history
🔄 Error Handling & Self-Recovery
Task Fails
    ↓
Recovery Agent checks retry_count
    ├── retry_count < 3  →  LLM proposes new approach → retry
    └── retry_count ≥ 3  →  Escalate to human (task marked "escalated")

LLM API Fails (429 Rate Limit)
    ↓
Exponential backoff: 1s → 2s → 4s
    ↓
Try next model: gemini-2.5-flash → gemini-2.0-flash → gemini-2.0-flash-001
    ↓
All exhausted → Agent logs failure → Workflow ends gracefully
📁 Project Structure
agentic_enterprise_ai/
├── backend/
│   ├── main.py                  # FastAPI app, CORS, routes
│   ├── requirements.txt
│   ├── .env                     # Your config (git-ignored)
│   ├── .env.example
│   ├── workflows.json           # Persisted workflow history
│   ├── agents/
│   │   ├── extraction_agent.py
│   │   ├── planning_agent.py
│   │   ├── execution_agent.py
│   │   ├── monitoring_agent.py
│   │   ├── recovery_agent.py
│   │   └── validation_agent.py
│   ├── core/
│   │   ├── graph.py             # LangGraph state machine
│   │   ├── runner.py            # Workflow entry point
│   │   ├── state.py             # WorkflowState TypedDict
│   │   ├── llm_router.py        # Gemini API + fallback chain
│   │   └── logger.py           # Structured audit logging
│   └── db/
│       └── json_store.py        # Workflow persistence
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── components/
    │   │   ├── Header.jsx
    │   │   ├── InputPanel.jsx
    │   │   ├── WorkflowResult.jsx
    │   │   └── HistoryPanel.jsx
    │   └── index.css
    └── package.json
⚙️ Configuration Options
Variable	Default	Description
GOOGLE_API_KEY	(required)	Gemini API key
CLOUD_LLM_MODEL	gemini-2.5-flash	Primary Gemini model
OLLAMA_MODEL	(empty)	Set to use a local Ollama model instead
SIMULATE_FAILURE	false	Set true to demo recovery agent
FAILURE_RATE	0.3	Probability of simulated task failure (0–1)
API_PORT	9000	Backend server port
🧪 Troubleshooting
Problem	Fix
UnicodeEncodeError on Windows	Set PYTHONUTF8=1 before starting uvicorn
500 Internal Server Error	Check terminal for traceback; likely missing GOOGLE_API_KEY
429 Rate Limited	Gemini free tier; the system auto-retries with backoff
Port already in use	Change --port 9000 to another port; update App.jsx URLs to match
CORS blocked in browser	Ensure backend is running on same port as frontend expects (9000)
No models in Ollama	Leave OLLAMA_MODEL= empty; system will use Gemini directly
🤝 Contributing
Fork the repository
Create your feature branch: git checkout -b feature/your-feature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/your-feature
Open a Pull Request
📜 License
MIT License — see LICENSE for details.

Built for the ET Hackathon 2026 — Agentic Enterprise AI Track
