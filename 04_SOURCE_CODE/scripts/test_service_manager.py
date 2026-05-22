import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from service_manager import ServiceManager


def main() -> None:
    print("=== SERVICE MANAGER TEST ===")

    manager = ServiceManager()

    manager.register_service(
        "memory_service"
    )

    manager.register_service(
        "knowledge_service"
    )

    manager.start_service(
        "memory_service"
    )

    manager.start_service(
        "knowledge_service"
    )

    print("\nCurrent Services:")

    for service, status in (
        manager.get_services().items()
    ):
        print(f"- {service}: {status}")

    manager.stop_service(
        "memory_service"
    )

    print("\nSERVICE MANAGER TEST PASSED")


if __name__ == "__main__":
    main()