import sys
from pathlib import Path

from logger import log_info, log_success, log_warning


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def validate_python_version() -> bool:
    major = sys.version_info.major
    minor = sys.version_info.minor

    log_info(f"Detected Python {major}.{minor}")

    if major == 3 and minor >= 12:
        log_success("Python version is compatible.")
        return True

    log_warning("Python 3.12 or higher is recommended.")
    return False


def validate_required_folders() -> bool:
    root = get_project_root()

    required_folders = [
        "00_PROJECT_CONTROL",
        "01_PREPRODUCTION",
        "02_ARCHITECTURE",
        "03_DEVELOPMENT",
        "04_SOURCE_CODE",
        "05_KNOWLEDGE",
        "06_PROJECT_MEMORY",
        "07_TESTING",
        "08_OUTPUTS",
        "09_BACKUPS",
    ]

    missing = []

    for folder in required_folders:
        folder_path = root / folder
        if not folder_path.exists():
            missing.append(folder)

    if missing:
        log_warning(f"Missing folders: {missing}")
        return False

    log_success("Required project folders found.")
    return True