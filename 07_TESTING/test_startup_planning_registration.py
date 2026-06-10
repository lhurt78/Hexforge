import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from startup import run_startup_sequence


result = run_startup_sequence()

assert result is True

print(
    "Startup planning registration validation passed."
)