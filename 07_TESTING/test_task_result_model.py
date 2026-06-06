import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from task_result import TaskResult


result = TaskResult(
    task_id="test-task",
    success=True,
    message="Task completed.",
    data={"value": 1},
)

print("Task ID:", result.task_id)
print("Success:", result.success)
print("Message:", result.message)
print("Data:", result.data)
print("Error:", result.error)

if (
    result.task_id == "test-task"
    and result.success is True
    and result.message == "Task completed."
    and result.data == {"value": 1}
    and result.error is None
):
    print("TaskResult model validation passed.")
else:
    print("TaskResult model validation failed.")
    raise SystemExit(1)