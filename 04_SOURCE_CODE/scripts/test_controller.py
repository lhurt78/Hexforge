import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from app_controller import AppController


def main() -> None:
    print("=== HEXFORGE CONTROLLER TEST ===")

    controller = AppController()

    controller.register_system(
        "memory_manager",
        "planned"
    )

    controller.register_system(
        "knowledge_manager",
        "planned"
    )

    controller.register_system(
        "research_manager",
        "planned"
    )

    controller.initialize()

    print("\nRegistered Systems:")

    for system, status in (
        controller.get_registered_systems().items()
    ):
        print(f"- {system}: {status}")

    controller.shutdown()

    print("\nCONTROLLER TEST PASSED")


if __name__ == "__main__":
    main()