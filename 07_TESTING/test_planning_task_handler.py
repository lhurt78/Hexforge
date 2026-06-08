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
    assert set(result.data.keys()) == {
    "overview",
    "goal",
    "category",
    "scope",
    "constraints",
    "priority",
    "target_outcome",
    "recommended_steps",
    "risks",
    "next_action",
    "success_criteria",
    "planning_assumptions",
    "planning_notes",
}
    assert result.data["goal"] == goal
    assert result.data["category"] == expected_category, (
        f"Expected category '{expected_category}' "
        f"but got '{result.data['category']}' "
        f"for goal: {goal}"
    )

    assert result.data["overview"] == (
        f"{expected_category.title()} planning request: {goal}"
    )

    assert isinstance(result.data["recommended_steps"], list)

    assert isinstance(result.data["risks"], list)
    assert result.data["risks"] == [
        "Missing constraints may allow uncontrolled scope expansion.",
        "Missing scope may cause planning drift.",
        "Missing target outcome may make completion harder to verify.",
    ]

    assert isinstance(result.data["success_criteria"], list)
    assert result.data["success_criteria"] == [
        "The planning goal is clearly documented.",
        "Recommended execution steps are available.",
    ]

    assert isinstance(result.data["planning_assumptions"], list)
    assert result.data["planning_assumptions"] == [
        "No project scope was provided.",
        "No project constraints were provided.",
        "No project priority was provided.",
        "No target outcome was provided.",
    ]

    assert len(result.data["recommended_steps"]) == 5
    assert result.data["next_action"] == result.data["recommended_steps"][0]
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
    (
        "Create a screenplayish document.",
        "general",
    ),
    (
        "Build a gameplan for chores.",
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

invalid_payload_cases = [
    (
        {
            "goal": "Plan a project.",
            "scope": 123,
        },
        "invalid_scope",
    ),
    (
        {
            "goal": "Plan a project.",
            "constraints": "keep it small",
        },
        "invalid_constraints",
    ),
    (
        {
            "goal": "Plan a project.",
            "constraints": [
                "",
            ],
        },
        "invalid_constraints",
    ),
    (
        {
            "goal": "Plan a project.",
            "priority": 10,
        },
        "invalid_priority",
    ),
    (
        {
            "goal": "Plan a project.",
            "target_outcome": [
                "finished",
            ],
        },
        "invalid_target_outcome",
    ),
]

for payload, expected_error in invalid_payload_cases:
    invalid_task = Task(
        task_type="planning_task",
        payload=payload,
    )

    invalid_result = task_executor.execute(invalid_task)

    assert invalid_result.success is False
    assert invalid_result.error == expected_error
    assert invalid_task.status == "failed"

cleanup_task = Task(
    task_type="planning_task",
    payload={
        "goal": "  Create a software utility.  ",
        "scope": "  Small internal tool.  ",
        "constraints": [
            "  No database.  ",
            "  Local only.  ",
        ],
        "priority": "  medium  ",
        "target_outcome": "  Working prototype.  ",
    },
)

cleanup_result = task_executor.execute(
    cleanup_task
)

assert cleanup_result.success is True

assert cleanup_result.data["goal"] == (
    "Create a software utility."
)

assert cleanup_result.data["scope"] == (
    "Small internal tool."
)

assert cleanup_result.data["constraints"] == [
    "No database.",
    "Local only.",
]

assert cleanup_result.data["priority"] == (
    "medium"
)

assert cleanup_result.data["target_outcome"] == (
    "Working prototype."
)

assert cleanup_task.status == "completed"

planning_notes_task = Task(
    task_type="planning_task",
    payload={
        "goal": "Create a short film production plan.",
        "scope": "15 minute horror short.",
        "constraints": [
            "Budget under $500.",
            "Two actors.",
        ],
        "priority": "high",
        "target_outcome": "Shoot-ready plan.",
    },
)

planning_notes_result = task_executor.execute(
    planning_notes_task
)

assert planning_notes_result.success is True

assert planning_notes_result.data["planning_notes"] == [
    "Scope should be used to limit the planning response.",
    "Constraints should be reviewed before execution begins.",
    "Priority should influence which step is handled first.",
    "Target outcome should be used to verify completion.",
]

assert planning_notes_task.status == "completed"