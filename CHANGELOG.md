
### [2026-09-29 15:25:13 UTC] feat(frontend): abilitare avvio locale e punti di accesso per test manuale
Implementazione: Come provo questo sitoweb quindi? prima di mandare i lavori agli altri agenti rispondi a me

File coinvolti:
- typescript (29 righe)
- env (10 righe)
- typescript (15 righe)
- typescript (12 righe)
- css (10 righe)
- typescript (24 righe)
- typescript (23 righe)
- typescript (21 righe)
- typescript (10 righe)
- typescript (10 righe)
- typescript (10 righe)
- typescript (76 righe)
- typescript (84 righe)
- infra/docker-compose.yml (43 righe)
- infra/docker-compose.ci.yml (20 righe)
- frontend/Dockerfile (14 righe)
- mock-backend/Dockerfile (6 righe)
- bash (1 righe)
- bash (1 righe)
- bash (1 righe)
- bash (1 righe)
- bash (1 righe)
- backend/app/main.py (191 righe)
- backend/requirements.txt (3 righe)
- backend/Dockerfile (18 righe)
- backend/README.md (20 righe)
- bash (2 righe)
- bash (1 righe)
- python (6 righe)
- python (12 righe)
- python (10 righe)
- bash (2 righe)
- bash (1 righe)
- bash (1 righe)
- tris/README.md (12 righe)
- backend/tests/test_main.py (98 righe)

QA Status: approved
Security Audit: PASS


### [2026-09-29 14:58:37 UTC] feat(frontend): preparare avvio locale e punti di accesso per test manuale
Implementazione: come li posso testare di persona?

File coinvolti:
- frontend/package.json (29 righe)
- frontend/next.config.js (10 righe)
- frontend/src/components/tris/Tris.tsx (156 righe)
- frontend/src/app/tris/page.tsx (6 righe)
- frontend/src/app/layout.tsx (21 righe)
- frontend/src/globals.css (5 righe)
- bash (2 righe)
- bash (1 righe)
- bash (3 righe)
- frontend/Dockerfile (23 righe)
- infra/docker-compose.yml (17 righe)
- dotenv (3 righe)
- makefile (6 righe)
- github/workflows/frontend-ci.yml (36 righe)
- bash (3 righe)
- bash (2 righe)
- json (6 righe)
- javascript (54 righe)
- javascript (19 righe)
- frontend/README.md (10 righe)
- tests/test_tris_component.py (34 righe)
- frontend/src/components/tris/__tests__/Tris.test.tsx (95 righe)

QA Status: approved
Security Audit: PASS

# CHANGELOG

## [2026-09-29] - refactor(models): migrate to gpt-5-mini/gpt-5-nano/Phi-4-mini per deprecazione gpt-4o-mini
### Changed
- Migrazione ad Azure AI Foundry con mapping specializzato:
  - HeadAgent & SecurityAgent ➔ `gpt-5-mini`
  - Worker Agents (Backend, Frontend, DevOps, Research) ➔ `gpt-5-nano`
  - QAAgent & DocsAgent ➔ `Phi-4-mini-instruct`
- Rimossi tutti i riferimenti ai modelli deprecati (gpt-4o-mini, gpt-4.1-mini, gpt-4o).
- Budget tracker aggiornato per tariffe Foundry e hard-stop >90% su Phi-4-mini.
- Motivazione: gpt-4.1-mini in deprecazione, gpt-4o-mini non più distribuibile.
