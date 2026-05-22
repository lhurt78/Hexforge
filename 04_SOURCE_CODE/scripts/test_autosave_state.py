import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from state_manager import StateManager


def main() -> None:
    print("=== AUTOSAVE STATE TEST ===")

    state = StateManager()

    state.load_all_state()

    state.memory_manager.store_memory(
        "autosave_test",
        "Autosave system is working."
    )

    success = state.autosave_state()

    if not success:
        print("\nAUTOSAVE STATE TEST FAILED")
        raise SystemExit(1)

    print("\nAUTOSAVE STATE TEST PASSED")


if __name__ == "__main__":
    main()