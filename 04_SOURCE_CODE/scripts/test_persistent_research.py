import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from research_manager import (
    ResearchManager
)


def main() -> None:
    print("=== PERSISTENT RESEARCH TEST ===")

    research = ResearchManager()

    research.add_research_topic(
        "Python Best Practices",
        "approved_sources.md",
        "high"
    )

    research.add_research_topic(
        "Unity ECS",
        "approved_sources.md",
        "normal"
    )

    research.save_research_queue()

    print("\nResearch Queue Saved.")

    restored = ResearchManager()

    restored.load_research_queue()

    print("\nRestored Research Queue:")

    for item in (
        restored.get_research_topics()
    ):
        print(item)

    print(
        f"\nResearch Count: "
        f"{restored.get_research_count()}"
    )

    print(
        "\nPERSISTENT RESEARCH TEST PASSED"
    )


if __name__ == "__main__":
    main()