from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROJECT_FOLDERS = {
    "project_control": PROJECT_ROOT / "00_PROJECT_CONTROL",
    "preproduction": PROJECT_ROOT / "01_PREPRODUCTION",
    "architecture": PROJECT_ROOT / "02_ARCHITECTURE",
    "development": PROJECT_ROOT / "03_DEVELOPMENT",
    "source_code": PROJECT_ROOT / "04_SOURCE_CODE",
    "knowledge": PROJECT_ROOT / "05_KNOWLEDGE",
    "memory": PROJECT_ROOT / "06_PROJECT_MEMORY",
    "testing": PROJECT_ROOT / "07_TESTING",
    "outputs": PROJECT_ROOT / "08_OUTPUTS",
    "backups": PROJECT_ROOT / "09_BACKUPS",
}

OUTPUT_FOLDERS = {
    "logs": PROJECT_FOLDERS["outputs"] / "logs",
    "exports": PROJECT_FOLDERS["outputs"] / "exports",
    "generated": PROJECT_FOLDERS["outputs"] / "generated",
    "temp": PROJECT_FOLDERS["outputs"] / "temp",
}

KNOWLEDGE_FOLDERS = {
    "raw": PROJECT_FOLDERS["knowledge"] / "raw",
    "processed": PROJECT_FOLDERS["knowledge"] / "processed",
    "approved": PROJECT_FOLDERS["knowledge"] / "approved",
    "rejected": PROJECT_FOLDERS["knowledge"] / "rejected",
    "embeddings": PROJECT_FOLDERS["knowledge"] / "embeddings",
}