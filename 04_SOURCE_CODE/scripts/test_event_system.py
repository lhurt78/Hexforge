import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "04_SOURCE_CODE" / "src"

sys.path.append(str(SRC_DIR))

from event_system import EventSystem


def on_test_event(data: dict) -> None:
    print(f"Received event data: {data}")


def main() -> None:
    print("=== EVENT SYSTEM TEST ===")

    events = EventSystem()

    events.subscribe("test_event", on_test_event)

    events.emit(
        "test_event",
        {"message": "Hexforge event system online."}
    )

    print("\nRegistered Events:")

    for event_name in events.get_registered_events():
        print(f"- {event_name}")

    print("\nEVENT SYSTEM TEST PASSED")


if __name__ == "__main__":
    main()