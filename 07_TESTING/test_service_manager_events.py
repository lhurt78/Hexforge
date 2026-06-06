import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from event_system import EventSystem
from service_manager import ServiceManager


events_seen = []


def record_event(event_name: str):
    def listener(data: dict) -> None:
        events_seen.append(event_name)

    return listener


event_system = EventSystem()

event_system.subscribe(
    "service_registered",
    record_event("service_registered"),
)

event_system.subscribe(
    "service_started",
    record_event("service_started"),
)

event_system.subscribe(
    "service_stopped",
    record_event("service_stopped"),
)

event_system.subscribe(
    "service_start_failed",
    record_event("service_start_failed"),
)

event_system.subscribe(
    "service_stop_failed",
    record_event("service_stop_failed"),
)

service_manager = ServiceManager(
    event_system=event_system,
)

service_manager.register_service(
    "runtime_status",
    "offline",
)

service_manager.start_service(
    "runtime_status",
)

service_manager.stop_service(
    "runtime_status",
)

service_manager.start_service(
    "unknown_service",
)

service_manager.stop_service(
    "unknown_service",
)

print("ServiceManager events seen:", events_seen)

expected_events = [
    "service_registered",
    "service_started",
    "service_stopped",
    "service_start_failed",
    "service_stop_failed",
]

if events_seen == expected_events:
    print("ServiceManager event validation passed.")
else:
    print("ServiceManager event validation failed.")
    raise SystemExit(1)