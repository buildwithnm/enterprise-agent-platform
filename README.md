# Enterprise Agent Platform

> A production-grade Agentic AI platform built from scratch using modern AI engineering practices.

This repository is being developed incrementally as part of the **Mastering Agentic AI Engineering** course. Every Git commit introduces one production-ready concept, starting from project setup and ending with a fully deployed multi-agent platform.

---

# Project Vision

Build an enterprise-ready AI platform featuring:

- LangChain
- LangGraph
- Local & Cloud LLMs
- RAG
- Multi-Agent Systems
- Observability
- Evaluation
- FastAPI
- Docker
- Kubernetes
- GitHub Actions

---

# Current Progress

# Progress

| Commit | Topic | Status |
|---------|-------|--------|
| ✅ 1 | Project Setup | Complete |
| ✅ 2 | LangChain Integration | Complete |
| ✅ 3 | Prompt Engineering | Complete |
| ✅ 4 | Structured Output & API Models | Complete |
| ⏳ 5 | LCEL & Output Parsers | Next |

# Current Architecture

```text
User
 │
 ▼
Request Model
 │
 ▼
FastAPI
 │
 ▼
LLM Service
 │
 ▼
Prompt Template
 │
 ▼
LangChain
 │
 ▼
Ollama
 │
 ▼
Response Model
```

---

# Repository Structure

```
enterprise-agent-platform/

│
├── app/
│
│   ├── api/
│   │
│   ├── config/
│   │
│   ├── llm/
│   │   ├── client.py
│   │   └── provider.py
│   │
│   ├── prompts/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── tests/
│
├── pyproject.toml
│
├── .env
│
└── README.md
```

---

# Features

### AI Features

- Prompt Templates
- Persona Management
- Typed Request Models
- Typed Response Models
- Execution Time Metrics

## Infrastructure

- FastAPI
- Modular Architecture
- Logging
- Configuration
- Unit Testing

## AI

- Ollama
- LangChain
- Prompt Templates
- System Prompt
- Human Prompt
- LCEL (Prompt → LLM)

---

# API

## Health Check

```
GET /api/v1/health
```

Response

```json
{
    "status": "UP"
}
```

---

## Chat

```
GET /api/v1/chat
```

Example

```
/api/v1/chat?question=Explain LangChain
```

Response

```json
{
    "answer": "..."
}
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| API | FastAPI |
| LLM | Ollama |
| Framework | LangChain |
| Configuration | Pydantic Settings |
| Logging | Loguru |
| Testing | Pytest |

---

# Run Locally

## Clone

```bash
git clone https://github.com/<YOUR_USERNAME>/enterprise-agent-platform.git

cd enterprise-agent-platform
```

---

## Install

```bash
pip install -e .
```

---

## Download Model

```bash
ollama pull qwen2.5:3b
```

---

## Start Server

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

# Learning Journey

This project follows a commit-by-commit learning approach.

```
Commit 1
│
├── Project Setup
├── FastAPI
├── Ollama
└── Local LLM

↓

Commit 2
│
├── LangChain
├── Provider Pattern
├── LLM Client
└── API Versioning

↓

Commit 3
Prompt Engineering

↓

Commit 4
Structured Output

↓

...

↓

Commit 30
Production Deployment
```

---

# Upcoming Modules

- Prompt Templates
- Output Parsers
- LCEL
- RAG
- Tool Calling
- Agents
- LangGraph
- Multi-Agent Systems
- Observability
- Evaluation
- Docker
- Kubernetes

---

# Roadmap

## Phase 1

- [x] Project Setup
- [x] LangChain Integration
- [ ] Prompt Templates
- [ ] Structured Output
- [ ] Configuration

## Phase 2

- [ ] LangChain Chains
- [ ] LCEL
- [ ] Streaming
- [ ] Memory

## Phase 3

- [ ] RAG
- [ ] Vector Database
- [ ] Embeddings
- [ ] Retrieval

## Phase 4

- [ ] Agents
- [ ] Tool Calling
- [ ] Multi-Agent
- [ ] LangGraph

## Phase 5

- [ ] Observability
- [ ] Evaluation
- [ ] Docker
- [ ] Kubernetes
- [ ] GitHub Actions

---

# License

MIT

---

⭐ If you're following this repository, consider starring it to track the project's progress.

# Next Milestone

Commit 4 introduces **Structured Output**, where we'll make the LLM return valid JSON instead of unpredictable text.