# Next.js Static Export with Docker and Azure Static Web Apps CI/CD

## Overview
This repository contains a Next.js app configured for static export and deployment to Azure Static Web Apps with the following features:
- Multi-stage Dockerfile for local builds and static export serving via nginx.
- GitHub Actions CI workflow with lint, tests, build, and Azure deploy.
- Deployment uses Azure Static Web Apps for optimized low-cost static hosting.

## Local development with Docker

### Build and run container