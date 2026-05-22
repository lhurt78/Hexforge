from logger import (
    log_info,
    log_success,
    log_warning,
)


class TaskRouter:
    def __init__(self) -> None:
        self.routes: dict[str, str] = {}

    def register_route(
        self,
        task_type: str,
        handler_name: str
    ) -> None:

        self.routes[task_type] = handler_name

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
            log_warning(
                f"No route found for: {task_type}"
            )
            return None

        log_success(
            f"Resolved route: "
            f"{task_type} -> {handler}"
        )

        return handler

    def get_routes(self) -> dict[str, str]:
        return self.routes