import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from model_manager import ModelManager


def main() -> None:
    print("=== MODEL MANAGER TEST ===")

    manager = ModelManager()

    manager.register_model(
        "phi-3-mini",
        "local"
    )

    manager.register_model(
        "gpt-4o",
        "openai"
    )

    manager.activate_model(
        "phi-3-mini"
    )

    print("\nRegistered Models:")

    for model, details in (
        manager.get_registered_models().items()
    ):
        print(f"- {model}: {details}")

    print(
        f"\nActive Model: "
        f"{manager.get_active_model()}"
    )

    print("\nMODEL MANAGER TEST PASSED")


if __name__ == "__main__":
    main()