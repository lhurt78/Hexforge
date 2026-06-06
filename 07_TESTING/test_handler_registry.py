import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from handler_registry import HandlerRegistry
from task import Task
from task_handler import TaskHandler
from task_result import TaskResult


class ExampleHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Example handler completed task.",
            data={
                "task_type": task.task_type,
            },
        )


registry = HandlerRegistry()
handler = ExampleHandler()

registry.register_handler(
    "example_handler",
    handler,
)

resolved_handler = registry.get_handler("example_handler")

assert resolved_handler is handler
assert registry.get_handler("missing_handler") is None

handlers = registry.get_handlers()

assert "example_handler" in handlers
assert handlers["example_handler"] is handler

task = Task(
    task_type="example_task",
    payload={
        "example": True,
    },
)

result = resolved_handler.handle(task)

assert result.task_id == task.task_id
assert result.success is True
assert result.message == "Example handler completed task."
assert result.data["task_type"] == "example_task"

print("HandlerRegistry validation passed.")