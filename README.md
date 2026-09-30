# WMS Application

Warehouse Management System multi-tenant sviluppato dal team AI gerarchico.

## 🤖 Modelli AI (Azure AI Foundry)
- **gpt-5-mini**: HeadAgent (Orchestrazione) & SecurityAgent (Audit & Compliance)
- **gpt-5-nano**: Backend, Frontend, DevOps, Research (Worker specialisti)
- **Phi-4-mini-instruct**: QAAgent (Review & Test) & DocsAgent (Documentazione)

> **Nota Architetturale (2026-09-29):** Migrazione a gpt-5-mini, gpt-5-nano e Phi-4-mini-instruct (gpt-4.1-mini in deprecazione, gpt-4o-mini non più distribuibile).

## Stack
- FastAPI
- PostgreSQL + Redis
- Next.js / React + Tailwind CSS
- Docker & Azure Container Apps
