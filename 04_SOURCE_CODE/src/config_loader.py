from pathlib import Path
from dotenv import load_dotenv

from environment import get_project_root
from logger import log_success


def load_environment_config() -> Path:
    root = get_project_root()
    env_path = root / ".env"

    if env_path.exists():
        load_dotenv(env_path)
        log_success(".env file loaded.")
    else:
        log_success("No .env file found. Using default environment.")

    return env_path