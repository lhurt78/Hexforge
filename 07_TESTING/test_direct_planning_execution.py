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
        "scope": "15 minute horror short.",
        "constraints": [
            "Budget under $500.",
            "Two actors.",
            "One location.",
        ],
        "priority": "high",
        "target_outcome": "Shoot-ready production plan.",
    },
)

result = task_executor.execute(task)

assert result.success is True
assert result.message == "Planning task completed."

assert result.data["goal"] == (
    "Create a short film production plan."
)

assert result.data["category"] == "film"
assert result.data["scope"] == "15 minute horror short."
assert result.data["priority"] == "high"
assert result.data["target_outcome"] == (
    "Shoot-ready production plan."
)

assert result.data["constraints"] == [
    "Budget under $500.",
    "Two actors.",
    "One location.",
]

assert len(
    result.data["recommended_steps"]
) == 5

assert len(
    result.data["planning_notes"]
) == 4

assert result.data["success_criteria"] == [
    "Planning goal has been documented.",
    "Recommended execution steps have been generated.",
    "Project scope has been documented.",
    "Target outcome has been documented.",
]

assert result.data["planning_assumptions"] == []

assert (
    "Constraints must shape the first executable plan."
    in result.data["planning_notes"]
)

assert task.status == "completed"

print(
    "Direct planning execution validation passed."
)