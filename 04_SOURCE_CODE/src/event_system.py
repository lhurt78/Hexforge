from collections.abc import Callable

from logger import log_info, log_success, log_warning


class EventSystem:
    def __init__(self) -> None:
        self.listeners: dict[str, list[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

        log_info(f"Subscribed listener to event: {event_name}")

    def emit(self, event_name: str, data: dict | None = None) -> None:
        if event_name not in self.listeners:
            log_warning(f"No listeners for event: {event_name}")
            return

        log_info(f"Emitting event: {event_name}")

        for callback in self.listeners[event_name]:
            callback(data or {})

    def get_registered_events(self) -> list[str]:
        return list(self.listeners.keys())