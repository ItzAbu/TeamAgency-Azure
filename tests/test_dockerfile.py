import pytest
from pathlib import Path

@pytest.fixture
def dockerfile_content():
    path = Path("Dockerfile")
    assert path.exists(), "Dockerfile mancante"
    return path.read_text(encoding="utf-8")

def test_dockerfile_multistage(dockerfile_content):
    assert "FROM node:18-alpine AS builder" in dockerfile_content
    assert "FROM nginx:alpine AS production" in dockerfile_content

def test_dockerfile_build_command(dockerfile_content):
    assert "RUN npm run build && npm run export" in dockerfile_content

def test_dockerfile_workdir(dockerfile_content):
    assert "WORKDIR /app" in dockerfile_content

def test_dockerfile_copy_commands(dockerfile_content):
    # Check COPY package*.json and COPY . .
    assert "COPY package*.json ./" in dockerfile_content
    assert "COPY . ." in dockerfile_content

def test_dockerfile_expose_and_cmd(dockerfile_content):
    assert "EXPOSE 80" in dockerfile_content
    assert 'CMD ["nginx", "-g", "daemon off;"]' in dockerfile_content