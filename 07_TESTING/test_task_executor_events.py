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


captured_events = []


def capture_event(data: dict) -> None:
    captured_events.append(data)


class ExampleHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Task executed successfully.",
        )


event_system = EventSystem()

event_system.subscribe(
    "task_execution_started",
    capture_event,
)

event_system.subscribe(
    "task_execution_completed",
    capture_event,
)

event_system.subscribe(
    "task_execution_failed",
    capture_event,
)

task_router = TaskRouter(event_system)
handler_registry = HandlerRegistry()

task_executor = TaskExecutor(
    task_router=task_router,
    handler_registry=handler_registry,
    event_system=event_system,
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
    payload={},
)

result = task_executor.execute(task)

assert result.success is True

assert len(captured_events) == 2

started_event = captured_events[0]
completed_event = captured_events[1]

assert started_event["task_id"] == task.task_id
assert started_event["task_type"] == "example_task"

assert completed_event["task_id"] == task.task_id
assert completed_event["task_type"] == "example_task"
assert completed_event["handler_name"] == "example_handler"

missing_route_task = Task(
    task_type="missing_route_task",
    payload={},
)

missing_route_result = task_executor.execute(missing_route_task)

assert missing_route_result.success is False
assert missing_route_result.error == "missing_route"

failed_event = captured_events[-1]

assert failed_event["task_id"] == missing_route_task.task_id
assert failed_event["task_type"] == "missing_route_task"
assert failed_event["error"] == "missing_route"

print("TaskExecutor event validation passed.")