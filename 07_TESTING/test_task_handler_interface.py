import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from task import Task
from task_result import TaskResult
from task_handler import TaskHandler


class TestHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:

        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Test handler executed.",
        )


task = Task(
    task_type="test",
    payload={},
)

handler = TestHandler()

result = handler.handle(task)

print("Task ID:", result.task_id)
print("Success:", result.success)
print("Message:", result.message)

if (
    result.task_id == task.task_id
    and result.success is True
    and result.message == "Test handler executed."
):
    print(
        "TaskHandler interface validation passed."
    )
else:
    print(
        "TaskHandler interface validation failed."
    )
    raise SystemExit(1)