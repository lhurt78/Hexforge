import sys
from pathlib import Path

from constants import PROJECT_FOLDERS
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
    required_folders = PROJECT_FOLDERS.values()

    missing = []

    for folder_path in required_folders:
        if not folder_path.exists():
            missing.append(folder_path.name)

    if missing:
        log_warning(f"Missing folders: {missing}")
        return False

    log_success("Required project folders found.")
    return True