import yaml
import pytest
from pathlib import Path

@pytest.fixture
def ci_cd_yaml_content():
    filepath = Path("github/workflows/ci-cd.yml")
    return filepath.read_text(encoding="utf-8")

def test_ci_cd_yaml_valid_yaml(ci_cd_yaml_content):
    # Verifica che il file YAML sia valido
    try:
        data = yaml.safe_load(ci_cd_yaml_content)
    except yaml.YAMLError as e:
        pytest.fail(f"ci-cd.yml invalido: {e}")

def test_ci_cd_yaml_jobs_exist(ci_cd_yaml_content):
    data = yaml.safe_load(ci_cd_yaml_content)
    assert "jobs" in data
    for job in ["lint", "test", "build_and_deploy", "deploy_to_azure_static_web_apps"]:
        assert job in data["jobs"], f"Job {job} mancante"

def test_ci_cd_yaml_node_version(ci_cd_yaml_content):
    data = yaml.safe_load(ci_cd_yaml_content)
    jobs = data["jobs"]
    for job_name in ["lint", "test", "build_and_deploy"]:
        steps = jobs[job_name].get("steps", [])
        node_version_steps = [step for step in steps if step.get("uses", "").startswith("actions/setup-node")]
        assert node_version_steps, f"Setup Node non definito in job {job_name}"
        for step in node_version_steps:
            assert step["with"]["node-version"] == 18, f"Node version errata in job {job_name}"

def test_ci_cd_yaml_secrets_set(ci_cd_yaml_content):
    data = yaml.safe_load(ci_cd_yaml_content)
    deploy_job = data["jobs"]["deploy_to_azure_static_web_apps"]
    steps = deploy_job.get("steps", [])
    deploy_step = next((s for s in steps if "Azure/static-web-apps-deploy@" in s.get("uses", "")), None)
    assert deploy_step is not None
    withs = deploy_step.get("with", {})
    assert "azure_static_web_apps_api_token" in withs
    assert "repo_token" in withs