import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from state_manager import StateManager


def main() -> None:
    print("=== SNAPSHOT RESTORE TEST ===")

    snapshots_dir = (
        ROOT_DIR
        / "09_BACKUPS"
        / "snapshots"
    )

    snapshot_folders = sorted(
        snapshots_dir.iterdir(),
        reverse=True
    )

    if not snapshot_folders:
        print("No snapshots found.")
        raise SystemExit(1)

    latest_snapshot = snapshot_folders[0]

    print(
        f"\nRestoring Snapshot:\n"
        f"{latest_snapshot}"
    )

    state = StateManager()

    state.restore_state_snapshot(
        latest_snapshot
    )

    print("\nRecovered Summary:")
    print(state.get_state_summary())

    print(
        "\nSNAPSHOT RESTORE TEST PASSED"
    )


if __name__ == "__main__":
    main()