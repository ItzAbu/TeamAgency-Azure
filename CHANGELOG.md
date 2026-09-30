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
