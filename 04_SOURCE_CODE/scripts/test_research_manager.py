import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from research_manager import (
    ResearchManager
)


def main() -> None:
    print("=== RESEARCH MANAGER TEST ===")

    research = ResearchManager()

    research.add_research_topic(
        "Python Best Practices",
        "approved_sources.md",
        "high"
    )

    research.add_research_topic(
        "Unity ECS Architecture",
        "approved_sources.md",
        "normal"
    )

    print("\nQueued Research Topics:")

    for item in (
        research.get_research_topics()
    ):
        print(item)

    research.complete_research(
        "Python Best Practices"
    )

    print(
        f"\nResearch Count: "
        f"{research.get_research_count()}"
    )

    print("\nRESEARCH MANAGER TEST PASSED")


if __name__ == "__main__":
    main()