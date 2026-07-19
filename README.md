# Enterprise Agent Platform

> Build a production-grade Agentic AI Platform from scratch using **FastAPI**, **LangChain**, **LangGraph**, and **Open Source LLMs**.

This repository is a step-by-step learning project where each Git commit introduces a new concept, gradually evolving from a simple LLM API into a production-ready multi-agent AI platform.

---

# Project Vision

The goal is not to build another chatbot.

The goal is to understand how enterprise AI systems are designed, developed, tested, monitored, and deployed.

By the end of this repository, you will have implemented:

* Enterprise FastAPI backend
* LangChain Expression Language (LCEL)
* LangGraph Agent Workflows
* RAG (Retrieval-Augmented Generation)
* Tool Calling
* Multi-Agent Systems
* Memory
* Observability
* Evaluation Framework
* Production Deployment

---

# Technology Stack

## Backend

* Python 3.12+
* FastAPI
* Uvicorn

## AI Framework

* LangChain
* LangChain Core
* LangGraph *(Upcoming)*

## LLM

* Ollama
* Qwen2.5 (Default)

## Configuration

* Pydantic
* pydantic-settings
* dotenv

## Logging

* Loguru

## Testing

* Pytest

---

# Repository Structure

```text
enterprise-agent-platform/

│

├── app/

│   ├── api/

│   ├── chains/

│   ├── config/

│   ├── container/

│   ├── llm/

│   ├── models/

│   ├── parsers/

│   ├── prompts/

│   ├── services/

│   ├── utils/

│   └── main.py

│

├── tests/

│

├── .env

├── pyproject.toml

└── README.md
```

---

# Current Architecture

```text
                    User

                      │

                      ▼

                  FastAPI

                      │

                      ▼

                 API Router

                      │

                      ▼

                 LLM Service

                      │

                      ▼

                 Chat Chain

                      │

        Prompt → LLM → Parser

                      │

                      ▼

                   Ollama
```

---

# Features Implemented

### Production Features

- Request Correlation IDs
- Logging Middleware
- Global Exception Handler
- Structured Request Logging
- Request Timing

### Performance Features

- Async FastAPI endpoints
- Async LangChain execution
- Async middleware
- Async testing

### Streaming Features

- Server-Sent Events (SSE)
- Token Streaming
- Async Generators
- LangChain `astream()`
- Streaming Error Handling


## Advanced LangChain Features

- RunnableLambda
- RunnableAssign
- RunnablePassthrough
- RunnableParallel
- RunnableBranch
- Retry Policies
- Model Fallbacks
- LCEL Playground

## Structured AI Outputs

- Pydantic Output Parser
- JSON Output Parser
- Structured Chains
- Output Validation
- Output Models


## Processing Pipeline

Every incoming request passes through a preprocessing pipeline before reaching the LLM.

Current stages

- Normalize whitespace
- Validate input

Future stages

- Prompt Injection Detection
- PII Masking
- Language Detection
- Query Rewriting
- Translation

## Commit 1 — Project Bootstrap

* FastAPI project setup
* Folder structure
* Environment configuration
* Ollama integration
* Health endpoint

---

## Commit 2 — LangChain Integration

* LangChain added
* Prompt templates
* LLM abstraction
* Basic chat endpoint

---

## Commit 3 — Prompt Engineering

Implemented a prompt management layer.

Features:

* Persona support
* General Assistant
* Data Engineer Assistant
* Prompt Manager
* Dynamic system prompts

---

## Commit 4 — Structured API Models

Introduced enterprise API contracts.

Features:

* Pydantic request models
* Pydantic response models
* Execution time metrics
* Provider metadata
* Timestamp metadata

---

## Commit 5 — LangChain Expression Language (LCEL)

Implemented reusable LangChain pipelines.

Features:

* Runnable chains
* Output parsers
* Base chain composition
* Separation of prompt and execution logic

---

## Commit 6 — Architecture Refactoring

Improved project architecture.

Features:

* Constructor-based dependency injection
* Application container
* BaseChain abstraction
* Improved separation of concerns
* Better extensibility for future chains

---

# Supported Personas

Current personas:

* General Assistant
* Data Engineer

Future personas:

* SQL Expert
* Cloud Architect
* Python Expert
* Reviewer
* Planner
* RAG Assistant

---

# Current API

## Health Check

```
GET /api/v1/health
```

---

## Chat

```
POST /api/v1/chat
```

Example request:

```json
{
  "question": "Explain LangChain",
  "persona": "general"
}
```

Example response:

```json
{
  "question": "Explain LangChain",
  "persona": "general",
  "answer": "...",
  "model": "qwen2.5:3b",
  "execution_time_ms": 1250,
  "provider": "ollama",
  "timestamp": "2026-07-10T10:25:00Z"
}
```

---

# Development Setup

## Clone Repository

```bash
git clone <repository-url>

cd enterprise-agent-platform
```

---

## Install Dependencies

```bash
pip install -e .
```

or

```bash
pip install -e ".[dev]"
```

---

## Configure Environment

Create a `.env` file.

```text
APP_NAME=Enterprise Agent Platform

OLLAMA_HOST=http://localhost:11434

MODEL_NAME=qwen2.5:3b

PROVIDER=ollama
```

---

## Start Ollama

```bash
ollama serve
```

Pull the model:

```bash
ollama pull qwen2.5:3b
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

# Learning Roadmap

## Phase 1 — Foundation ✅

* ✅ Project Setup
* ✅ LangChain
* ✅ Prompt Engineering
* ✅ Personas
* ✅ Structured API
* ✅ LCEL
* ✅ Dependency Injection

---

## Phase 2 — Production Engineering (Next)

* Request Middleware
* Correlation IDs
* JSON Logging
* Global Exception Handling
* Async FastAPI
* Streaming Responses
* Retry Policies

---

## Phase 3 — Enterprise LangChain

* RunnableParallel
* RunnableBranch
* Output Parsers
* Structured Output
* Prompt Versioning
* Prompt Registry

---

## Phase 4 — RAG

* Document Loaders
* Chunking
* Embeddings
* Vector Database
* Retrieval
* Context Injection

---

## Phase 5 — Agentic AI

* Tool Calling
* Planner Agent
* SQL Agent
* Research Agent
* LangGraph
* Multi-Agent Systems

---

## Phase 6 — Production

* Docker
* Kubernetes
* Redis
* PostgreSQL
* LangSmith
* OpenTelemetry
* Monitoring
* CI/CD

---

# Progress Tracker

| Commit | Topic | Status |
|---------|-------|--------|
| ✅ 1 | Project Bootstrap | Complete |
| ✅ 2 | LangChain Integration | Complete |
| ✅ 3 | Prompt Engineering | Complete |
| ✅ 4 | Structured Models | Complete |
| ✅ 5 | LCEL | Complete |
| ✅ 6 | Dependency Injection | Complete |
| ✅ 7 | Middleware & Logging | Complete |
| ✅ 8 | Async FastAPI | Complete |
| ✅ 9 | Streaming Responses (SSE) | Complete |
| ⏳ 10 | Advanced LCEL | Next |

# Long-Term Goals

By the end of this project, this repository will demonstrate:

* Production-grade AI backend architecture
* Enterprise coding standards
* Clean Architecture principles
* SOLID design
* LangChain best practices
* LangGraph orchestration
* Production observability
* Scalable deployment

The objective is to build a repository that is suitable for learning, interview preparation, portfolio demonstration, and as a foundation for real-world AI applications.
