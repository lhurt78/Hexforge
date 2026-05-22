import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from state_manager import StateManager


def main() -> None:
    print("=== STATE SNAPSHOT TEST ===")

    state = StateManager()

    state.load_all_state()

    success = state.create_state_snapshot()

    if not success:
        print("\nSTATE SNAPSHOT TEST FAILED")
        raise SystemExit(1)

    print("\nSTATE SNAPSHOT TEST PASSED")


if __name__ == "__main__":
    main()