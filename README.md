## Final Architecture
User -> HTTP Request -> FastAPI API -> AI Service -> Ollama (Local LLM) -> HTTP Response

## Step 1 Install Prerequisites
### Install Python
Use Python 3.12+
Verify: python --version

### Install Git
Verify: git --version

### Install VS Code Recommended extensions
Python
Pylance
Docker
GitLens
REST Client

## Step 2 Install Ollama
### Download
    👉 https://ollama.com

### Install and Verify
ollama --version

### Download a Free Model
For this course, I recommend "ollama pull qwen2.5:3b"

Why?
- Fast
- Small
- Excellent reasoning
- Tool calling capable
- Free

Test
ollama run qwen2.5:3b

Ask
Hello

If you receive an answer,
Congratulations.

You have your own ChatGPT running locally.

## Step 3 Create Repository
```bash
mkdir enterprise-agent-platform
cd enterprise-agent-platform
```

### Initialize Git
```bash
git init
```

## Step 4 Create Virtual Environment
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 5 Install Packages
```bash
python -m pip install-r requirements.txt
```


## Format Code
```bash
black .
```

## Lint
```bash
ruff check .
```


## What We Learned
- Project organization
- Virtual environments
- FastAPI basics
- Local LLMs with Ollama
- Environment-based configuration
- Logging
- Basic testing

## Assignment
1. Change the model from qwen2.5:3b to llama3.2:3b (or another Ollama model you have) and compare responses.
2. Add a /models endpoint that returns the configured model name from settings.
3. Enhance /health to also verify that the Ollama server is reachable.