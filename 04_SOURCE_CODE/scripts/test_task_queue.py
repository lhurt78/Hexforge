import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from task_queue import TaskQueue


def main() -> None:
    print("=== TASK QUEUE TEST ===")

    queue = TaskQueue()

    queue.add_task(
        "memory_update",
        {"topic": "python"}
    )

    queue.add_task(
        "research_scan",
        {"source": "approved_sources"}
    )

    print(f"\nQueue Size: {queue.get_queue_size()}")

    completed_task = queue.process_next_task()

    print("\nCompleted Task:")
    print(completed_task)

    print(f"\nRemaining Queue Size: {queue.get_queue_size()}")

    print("\nTASK QUEUE TEST PASSED")


if __name__ == "__main__":
    main()