import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from event_system import EventSystem
from task_router import TaskRouter


events_seen = []


def record_event(event_name: str):
    def listener(data: dict) -> None:
        events_seen.append(event_name)

    return listener


event_system = EventSystem()

event_system.subscribe(
    "task_route_registered",
    record_event("task_route_registered"),
)

event_system.subscribe(
    "task_route_resolved",
    record_event("task_route_resolved"),
)

event_system.subscribe(
    "task_route_missing",
    record_event("task_route_missing"),
)

task_router = TaskRouter(
    event_system=event_system,
)

task_router.register_route(
    "status_check",
    "status_handler",
)

task_router.resolve_route(
    "status_check",
)

task_router.resolve_route(
    "unknown_task",
)

print("TaskRouter events seen:", events_seen)

expected_events = [
    "task_route_registered",
    "task_route_resolved",
    "task_route_missing",
]

if events_seen == expected_events:
    print("TaskRouter event validation passed.")
else:
    print("TaskRouter event validation failed.")
    raise SystemExit(1)