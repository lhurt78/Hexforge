import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR / "04_SOURCE_CODE"))

from configs.settings import Settings


def main():
    print("=== HEXFORGE SETTINGS TEST ===")
    print(f"App Name: {Settings.APP_NAME}")
    print(f"Version: {Settings.VERSION}")
    print(f"Environment: {Settings.ENVIRONMENT}")
    print(f"Model Provider: {Settings.DEFAULT_MODEL_PROVIDER}")
    print(f"Default Model: {Settings.DEFAULT_MODEL_NAME}")
    print(f"Web Access Enabled: {Settings.ALLOW_WEB_ACCESS}")


if __name__ == "__main__":
    main()