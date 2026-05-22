import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from persistence_manager import (
    PersistenceManager
)


def main() -> None:
    print("=== PERSISTENCE MANAGER TEST ===")

    persistence = PersistenceManager()

    test_file = (
        ROOT_DIR
        / "08_OUTPUTS"
        / "temp"
        / "test_data.json"
    )

    test_data = {
        "project": "Hexforge",
        "status": "operational",
    }

    persistence.save_json(
        test_file,
        test_data
    )

    loaded_data = persistence.load_json(
        test_file
    )

    print("\nLoaded Data:")
    print(loaded_data)

    print(
        "\nPERSISTENCE MANAGER TEST PASSED"
    )


if __name__ == "__main__":
    main()