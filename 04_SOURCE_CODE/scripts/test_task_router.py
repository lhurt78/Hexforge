import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from task_router import TaskRouter


def main() -> None:
    print("=== TASK ROUTER TEST ===")

    router = TaskRouter()

    router.register_route(
        "memory_task",
        "memory_manager"
    )

    router.register_route(
        "research_task",
        "research_manager"
    )

    router.register_route(
        "knowledge_task",
        "knowledge_manager"
    )

    handler = router.resolve_route(
        "research_task"
    )

    print(f"\nResolved Handler: {handler}")

    print("\nRegistered Routes:")

    for task, route in (
        router.get_routes().items()
    ):
        print(f"- {task} -> {route}")

    print("\nTASK ROUTER TEST PASSED")


if __name__ == "__main__":
    main()