import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from state_manager import StateManager


def main() -> None:
    print("=== STATE SUMMARY TEST ===")

    state = StateManager()

    state.load_all_state()

    summary = state.get_state_summary()

    print("\nState Summary:")
    print(summary)

    print("\nSTATE SUMMARY TEST PASSED")


if __name__ == "__main__":
    main()