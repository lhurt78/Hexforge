from task_handler import TaskHandler


class HandlerRegistry:
    def __init__(self) -> None:
        self.handlers: dict[str, TaskHandler] = {}

    def register_handler(
        self,
        handler_name: str,
        handler: TaskHandler,
    ) -> None:
        self.handlers[handler_name] = handler

    def get_handler(
        self,
        handler_name: str,
    ) -> TaskHandler | None:
        return self.handlers.get(handler_name)

    def get_handlers(self) -> dict[str, TaskHandler]:
        return self.handlers