
### [2026-09-30 12:50:56 UTC] feat(frontend): implementazione ui/ux e logica gioco (react/next.js)
Implementazione: Crea una semplice webapp per giocare a tris, deve essere bella esticamente, poi deve avere anche delle funzionalità aggiunte, come giocare con un bot e lo storico delle partite con il counter delle partite vinte, non serve che si salva in un db, basta in locale

File coinvolti:
- Dockerfile (20 righe)
- package.json (10 righe)
- github/workflows/ci-cd.yml (83 righe)
- infra/azure/static-web-apps/azure-static-web-apps.yml (3 righe)
- README.md (11 righe)
- Next.js (17 righe)
- docs/README.md (7 righe)
- docs/USER_GUIDE.md (42 righe)
- docs/CHANGELOG.md (16 righe)
- docs/CONTRIBUTING.md (17 righe)
- docs/FAQ.md (35 righe)
- docs/api.yaml (65 righe)
- tests/test_ci_cd_yaml.py (41 righe)
- tests/test_dockerfile.py (27 righe)

QA Status: rejected
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
