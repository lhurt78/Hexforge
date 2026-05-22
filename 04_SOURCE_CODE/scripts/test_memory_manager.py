import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from memory_manager import MemoryManager


def main() -> None:
    print("=== MEMORY MANAGER TEST ===")

    memory = MemoryManager()

    memory.store_memory(
        "favorite_language",
        "Python"
    )

    result = memory.retrieve_memory(
        "favorite_language"
    )

    print(f"\nRetrieved Memory: {result}")

    print(
        f"\nMemory Count: "
        f"{memory.get_memory_count()}"
    )

    memory.delete_memory(
        "favorite_language"
    )

    print(
        f"\nFinal Memory Count: "
        f"{memory.get_memory_count()}"
    )

    print("\nMEMORY MANAGER TEST PASSED")


if __name__ == "__main__":
    main()