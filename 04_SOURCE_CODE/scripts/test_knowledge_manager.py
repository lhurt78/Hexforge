import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from knowledge_manager import (
    KnowledgeManager
)


def main() -> None:
    print("=== KNOWLEDGE MANAGER TEST ===")

    knowledge = KnowledgeManager()

    knowledge.add_knowledge(
        "python",
        "Python is a programming language.",
        "internal_test"
    )

    result = knowledge.get_knowledge(
        "python"
    )

    print("\nRetrieved Knowledge:")
    print(result)

    print(
        f"\nKnowledge Count: "
        f"{knowledge.get_knowledge_count()}"
    )

    knowledge.remove_knowledge(
        "python"
    )

    print(
        f"\nFinal Knowledge Count: "
        f"{knowledge.get_knowledge_count()}"
    )

    print("\nKNOWLEDGE MANAGER TEST PASSED")


if __name__ == "__main__":
    main()