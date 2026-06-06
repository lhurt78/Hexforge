from event_system import EventSystem

from logger import (
    log_info,
    log_success,
    log_warning,
)


class TaskRouter:
    def __init__(
        self,
        event_system: EventSystem,
    ) -> None:
        self.routes: dict[str, str] = {}
        self.event_system = event_system

    def register_route(
        self,
        task_type: str,
        handler_name: str
    ) -> None:

        self.routes[task_type] = handler_name

        self.event_system.emit(
            "task_route_registered",
            {
                "task_type": task_type,
                "handler_name": handler_name,
            }
        )

        log_info(
            f"Route registered: "
            f"{task_type} -> {handler_name}"
        )

    def resolve_route(
        self,
        task_type: str
    ) -> str | None:

        handler = self.routes.get(task_type)

        if handler is None:
            self.event_system.emit(
                "task_route_missing",
                {
                    "task_type": task_type,
                }
            )

            log_warning(
                f"No route found for: {task_type}"
            )
            return None

        self.event_system.emit(
            "task_route_resolved",
            {
                "task_type": task_type,
                "handler_name": handler,
            }
        )

        log_success(
            f"Resolved route: "
            f"{task_type} -> {handler}"
        )

        return handler

    def get_routes(self) -> dict[str, str]:
        return self.routes