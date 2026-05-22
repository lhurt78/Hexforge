import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from knowledge_manager import (
    KnowledgeManager
)


def main() -> None:
    print("=== PERSISTENT KNOWLEDGE TEST ===")

    knowledge = KnowledgeManager()

    knowledge.add_knowledge(
        "python",
        "Python is a programming language.",
        "internal_test"
    )

    knowledge.add_knowledge(
        "unity",
        "Unity is a game engine.",
        "internal_test"
    )

    knowledge.save_knowledge()

    print("\nKnowledge Saved.")

    restored = KnowledgeManager()

    restored.load_knowledge()

    print("\nRestored Knowledge:")

    print(
        restored.get_knowledge("python")
    )

    print(
        restored.get_knowledge("unity")
    )

    print(
        f"\nKnowledge Count: "
        f"{restored.get_knowledge_count()}"
    )

    print(
        "\nPERSISTENT KNOWLEDGE TEST PASSED"
    )


if __name__ == "__main__":
    main()