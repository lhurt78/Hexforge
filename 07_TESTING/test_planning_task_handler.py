import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.insert(0, str(SRC_PATH))

from event_system import EventSystem
from handler_registry import HandlerRegistry
from planning_task_handler import PlanningTaskHandler
from task import Task
from task_executor import TaskExecutor
from task_router import TaskRouter


event_system = EventSystem()

task_router = TaskRouter(
    event_system=event_system,
)

handler_registry = HandlerRegistry()

handler_registry.register_handler(
    "planning_handler",
    PlanningTaskHandler(),
)

task_router.register_route(
    "planning_task",
    "planning_handler",
)

task_executor = TaskExecutor(
    task_router=task_router,
    handler_registry=handler_registry,
    event_system=event_system,
)

task = Task(
    task_type="planning_task",
    payload={
        "goal": "Create a short film production plan.",
    },
)

result = task_executor.execute(task)

assert result.success is True
assert result.message == "Planning task completed."
assert result.data["goal"] == "Create a short film production plan."
assert len(result.data["recommended_steps"]) == 5
assert task.status == "completed"

missing_goal_task = Task(
    task_type="planning_task",
    payload={},
)

missing_goal_result = task_executor.execute(missing_goal_task)

assert missing_goal_result.success is False
assert missing_goal_result.error == "missing_goal"
assert missing_goal_task.status == "failed"

print("PlanningTaskHandler validation passed.")