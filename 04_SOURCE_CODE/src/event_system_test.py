from event_system import EventSystem


def run_event_system_test() -> bool:
    event_system = EventSystem()
    received_events = []

    def test_listener(data: dict) -> None:
        received_events.append(data)

    event_system.subscribe(
        "test_event",
        test_listener,
    )

    success = event_system.emit(
        "test_event",
        {
            "message": "Event system test successful."
        },
    )

    return (
        success
        and len(received_events) == 1
        and received_events[0]["message"] == "Event system test successful."
    )


if __name__ == "__main__":
    result = run_event_system_test()

    if result:
        print("Event system test passed.")
    else:
        print("Event system test failed.")