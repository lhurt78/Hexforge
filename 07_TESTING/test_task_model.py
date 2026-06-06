import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from task import Task


task = Task(
    task_type="status_check",
    payload={"message": "test"},
)

print("Task ID:", task.task_id)
print("Initial status:", task.status)

valid_update = task.update_status("running")
invalid_update = task.update_status("nonsense")

print("Valid update result:", valid_update)
print("Status after valid update:", task.status)
print("Invalid update result:", invalid_update)
print("Status after invalid update:", task.status)

if (
    task.task_type == "status_check"
    and task.payload == {"message": "test"}
    and valid_update is True
    and invalid_update is False
    and task.status == "running"
):
    print("Task model validation passed.")
else:
    print("Task model validation failed.")
    raise SystemExit(1)