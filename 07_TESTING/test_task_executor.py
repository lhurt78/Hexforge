import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from event_system import EventSystem
from handler_registry import HandlerRegistry
from task import Task
from task_executor import TaskExecutor
from task_handler import TaskHandler
from task_result import TaskResult
from task_router import TaskRouter


class ExampleHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Task executed successfully.",
            data={
                "task_type": task.task_type,
            },
        )


class FailingHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        raise ValueError("Example failure")


event_system = EventSystem()
task_router = TaskRouter(event_system)
handler_registry = HandlerRegistry()
task_executor = TaskExecutor(
    task_router,
    handler_registry,
)

handler_registry.register_handler(
    "example_handler",
    ExampleHandler(),
)

task_router.register_route(
    "example_task",
    "example_handler",
)

task = Task(
    task_type="example_task",
    payload={
        "example": True,
    },
)

result = task_executor.execute(task)

assert result.success is True
assert result.task_id == task.task_id
assert result.message == "Task executed successfully."
assert result.data["task_type"] == "example_task"
assert task.status == "completed"

missing_route_task = Task(
    task_type="missing_route_task",
    payload={},
)

missing_route_result = task_executor.execute(missing_route_task)

assert missing_route_result.success is False
assert missing_route_result.error == "missing_route"

task_router.register_route(
    "missing_handler_task",
    "missing_handler",
)

missing_handler_task = Task(
    task_type="missing_handler_task",
    payload={},
)

missing_handler_result = task_executor.execute(missing_handler_task)

assert missing_handler_result.success is False
assert missing_handler_result.error == "missing_handler"

handler_registry.register_handler(
    "failing_handler",
    FailingHandler(),
)

task_router.register_route(
    "failing_task",
    "failing_handler",
)

failing_task = Task(
    task_type="failing_task",
    payload={},
)

failing_result = task_executor.execute(failing_task)

assert failing_result.success is False
assert failing_result.error == "Example failure"
assert failing_task.status == "failed"

print("TaskExecutor validation passed.")