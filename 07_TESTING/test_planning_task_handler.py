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


def run_planning_task(
    goal: str,
    expected_category: str,
) -> None:
    task = Task(
        task_type="planning_task",
        payload={
            "goal": goal,
        },
    )

    result = task_executor.execute(task)

    assert result.success is True
    assert result.message == "Planning task completed."
    assert result.data["goal"] == goal
    assert result.data["category"] == expected_category, (
        f"Expected category '{expected_category}' "
        f"but got '{result.data['category']}' "
        f"for goal: {goal}"
    )

    assert result.data["overview"] == (
        f"{expected_category.title()} planning request identified: {goal}"
    )

    assert isinstance(result.data["recommended_steps"], list)

    assert isinstance(result.data["risks"], list)
    assert result.data["risks"] == [
        "No constraints were specified.",
        "Undefined scope may cause planning drift.",
        "Missing target outcome may make success harder to verify.",
    ]

    assert isinstance(result.data["constraints_summary"], list)
    assert result.data["constraints_summary"] == []

    assert isinstance(result.data["success_criteria"], list)
    assert result.data["success_criteria"] == [
        "Planning goal has been documented.",
        "Recommended execution steps have been generated.",
    ]

    assert isinstance(result.data["planning_assumptions"], list)
    assert result.data["planning_assumptions"] == [
        "Project scope was not provided.",
        "Project constraints were not provided.",
        "Project priority was not provided.",
        "Target outcome was not provided.",
    ]

    assert len(result.data["recommended_steps"]) == 5
    assert all(
        isinstance(step, str)
        and step.strip()
        for step in result.data["recommended_steps"]
    )
    assert task.status == "completed"


test_cases = [
    (
        "Create a software utility.",
        "software",
    ),
    (
        "Write a Python script.",
        "software",
    ),
    (
        "Build a game prototype.",
        "game",
    ),
    (
        "Create a Unity demo.",
        "game",
    ),
    (
        "Create a short film production plan.",
        "film",
    ),
    (
        "Plan a movie scene.",
        "film",
    ),
    (
        "Write a novel outline.",
        "writing",
    ),
    (
        "Draft a story chapter.",
        "writing",
    ),
    (
        "Organize a community project.",
        "general",
    ),
    (
        "Plan a household cleanup.",
        "general",
    ),
]

for goal, expected_category in test_cases:
    run_planning_task(
        goal,
        expected_category,
    )

missing_goal_task = Task(
    task_type="planning_task",
    payload={},
)

missing_goal_result = task_executor.execute(missing_goal_task)

assert missing_goal_result.success is False
assert missing_goal_result.error == "missing_goal"
assert missing_goal_task.status == "failed"

empty_goal_task = Task(
    task_type="planning_task",
    payload={
        "goal": "",
    },
)

empty_goal_result = task_executor.execute(empty_goal_task)

assert empty_goal_result.success is False
assert empty_goal_result.error == "missing_goal"
assert empty_goal_task.status == "failed"

print("PlanningTaskHandler validation passed.")