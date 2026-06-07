import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from planning_task_handler import PlanningTaskHandler
from task import Task


handler = PlanningTaskHandler()


def run_invalid_payload_test(
    payload: dict,
    expected_error: str,
) -> None:
    task = Task(
        task_type="planning_task",
        payload=payload,
    )

    result = handler.handle(task)

    assert result.success is False
    assert result.error == expected_error, (
        f"Expected error '{expected_error}' "
        f"but got '{result.error}'"
    )


run_invalid_payload_test(
    {
        "goal": "Create a short film.",
        "scope": 123,
    },
    "invalid_scope",
)

run_invalid_payload_test(
    {
        "goal": "Create a short film.",
        "constraints": "low budget",
    },
    "invalid_constraints",
)

run_invalid_payload_test(
    {
        "goal": "Create a short film.",
        "constraints": [
            "One location",
            "",
        ],
    },
    "invalid_constraints",
)

run_invalid_payload_test(
    {
        "goal": "Create a short film.",
        "priority": 10,
    },
    "invalid_priority",
)

run_invalid_payload_test(
    {
        "goal": "Create a short film.",
        "target_outcome": 42,
    },
    "invalid_target_outcome",
)

print("Planning payload validation passed.")