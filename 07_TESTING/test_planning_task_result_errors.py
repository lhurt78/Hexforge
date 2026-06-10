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


error_cases = [
    (
        {},
        "Planning task requires a goal.",
        "missing_goal",
    ),
    (
        {
            "goal": "Plan a project.",
            "scope": 123,
        },
        "Planning task scope must be a string.",
        "invalid_scope",
    ),
    (
        {
            "goal": "Plan a project.",
            "constraints": "keep it small",
        },
        "Planning task constraints must be a list.",
        "invalid_constraints",
    ),
    (
        {
            "goal": "Plan a project.",
            "priority": 10,
        },
        "Planning task priority must be a string.",
        "invalid_priority",
    ),
    (
        {
            "goal": "Plan a project.",
            "target_outcome": [
                "finished",
            ],
        },
        "Planning task target_outcome must be a string.",
        "invalid_target_outcome",
    ),
]

for payload, expected_message, expected_error in error_cases:
    task = Task(
        task_type="planning_task",
        payload=payload,
    )

    result = task_executor.execute(
        task
    )

    assert result.success is False
    assert result.message == expected_message
    assert result.error == expected_error
    assert task.status == "failed"


print(
    "Planning TaskResult error validation passed."
)