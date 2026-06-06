import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from echo_task_handler import EchoTaskHandler
from event_system import EventSystem
from handler_registry import HandlerRegistry
from task import Task
from task_executor import TaskExecutor
from task_router import TaskRouter


event_system = EventSystem()

task_router = TaskRouter(
    event_system=event_system,
)

handler_registry = HandlerRegistry()

handler_registry.register_handler(
    "echo_handler",
    EchoTaskHandler(),
)

task_router.register_route(
    "echo_task",
    "echo_handler",
)

task_executor = TaskExecutor(
    task_router=task_router,
    handler_registry=handler_registry,
)

task = Task(
    task_type="echo_task",
    payload={
        "message": "hello world",
        "value": 42,
    },
)

result = task_executor.execute(task)

assert result.success is True
assert result.message == "Echo task completed."

assert result.data["task_type"] == "echo_task"
assert result.data["payload"]["message"] == "hello world"
assert result.data["payload"]["value"] == 42

assert task.status == "completed"

print("Echo task execution validation passed.")