from collections.abc import Callable

from logger import log_info, log_success, log_warning, log_error


class EventSystem:
    def __init__(self) -> None:
        self.listeners: dict[str, list[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        if not event_name:
            log_warning("Cannot subscribe to an empty event name.")
            return

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

        log_info(f"Subscribed listener to event: {event_name}")

    def emit(self, event_name: str, data: dict | None = None) -> bool:
        if not event_name:
            log_warning("Cannot emit an empty event name.")
            return False

        if event_name not in self.listeners:
            log_warning(f"No listeners for event: {event_name}")
            return False

        log_info(f"Emitting event: {event_name}")

        event_data = data or {}
        success = True

        for callback in self.listeners[event_name]:
            try:
                callback(event_data)
            except Exception as error:
                success = False
                log_error(
                    f"Event listener failed for event '{event_name}': {error}"
                )

        if success:
            log_success(f"Event emitted successfully: {event_name}")

        return success

    def get_registered_events(self) -> list[str]:
        return list(self.listeners.keys())