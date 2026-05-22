import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from memory_manager import MemoryManager


def main() -> None:
    print("=== PERSISTENT MEMORY TEST ===")

    memory = MemoryManager()

    memory.store_memory(
        "project_name",
        "Hexforge"
    )

    memory.store_memory(
        "primary_language",
        "Python"
    )

    memory.save_memories()

    print("\nSaved Memories.")

    restored_memory = MemoryManager()

    restored_memory.load_memories()

    print("\nRestored Memories:")

    print(
        restored_memory.retrieve_memory(
            "project_name"
        )
    )

    print(
        restored_memory.retrieve_memory(
            "primary_language"
        )
    )

    print(
        f"\nMemory Count: "
        f"{restored_memory.get_memory_count()}"
    )

    print(
        "\nPERSISTENT MEMORY TEST PASSED"
    )


if __name__ == "__main__":
    main()