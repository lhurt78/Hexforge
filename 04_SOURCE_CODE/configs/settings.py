import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(ROOT_DIR / ".env")


class Settings:
    APP_NAME = os.getenv("HEXFORGE_NAME", "Hexforge")
    VERSION = os.getenv("HEXFORGE_VERSION", "0.1.0")
    ENVIRONMENT = os.getenv("HEXFORGE_ENV", "development")

    KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "05_KNOWLEDGE")
    MEMORY_PATH = os.getenv("MEMORY_PATH", "06_PROJECT_MEMORY")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH", "08_OUTPUTS")
    BACKUP_PATH = os.getenv("BACKUP_PATH", "09_BACKUPS")

    DEFAULT_MODEL_PROVIDER = os.getenv(
        "DEFAULT_MODEL_PROVIDER",
        "local"
    )

    DEFAULT_MODEL_NAME = os.getenv(
        "DEFAULT_MODEL_NAME",
        "phi-3-mini"
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    ENABLE_FILE_LOGGING = (
        os.getenv("ENABLE_FILE_LOGGING", "true").lower() == "true"
    )

    ALLOW_WEB_ACCESS = (
        os.getenv("ALLOW_WEB_ACCESS", "false").lower() == "true"
    )

    ALLOW_SELF_MODIFICATION = (
        os.getenv("ALLOW_SELF_MODIFICATION", "false").lower() == "true"
    )

    ALLOW_AUTONOMOUS_ACTIONS = (
        os.getenv("ALLOW_AUTONOMOUS_ACTIONS", "false").lower() == "true"
    )