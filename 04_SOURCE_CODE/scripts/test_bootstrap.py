import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from startup import run_startup_sequence


def main() -> None:
    print("=== HEXFORGE BOOTSTRAP TEST ===")

    success = run_startup_sequence()

    if not success:
        print("BOOTSTRAP TEST FAILED")
        raise SystemExit(1)

    print("BOOTSTRAP TEST PASSED")


if __name__ == "__main__":
    main()