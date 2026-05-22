import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from state_manager import (
    StateManager
)


def main() -> None:
    print("=== STATE MANAGER TEST ===")

    state = StateManager()

    state.memory_manager.store_memory(
        "current_project",
        "Hexforge"
    )

    state.knowledge_manager.add_knowledge(
        "python",
        "Python is a programming language.",
        "internal_test"
    )

    state.research_manager.add_research_topic(
        "AI orchestration systems",
        "approved_sources.md",
        "high"
    )

    state.save_all_state()

    print("\nState Saved.")

    restored = StateManager()

    restored.load_all_state()

    print("\nRecovered Memory:")
    print(
        restored.memory_manager
        .retrieve_memory(
            "current_project"
        )
    )

    print("\nRecovered Knowledge:")
    print(
        restored.knowledge_manager
        .get_knowledge("python")
    )

    print("\nRecovered Research Queue:")
    print(
        restored.research_manager
        .get_research_topics()
    )

    print(
        "\nSTATE MANAGER TEST PASSED"
    )


if __name__ == "__main__":
    main()