from event_system import EventSystem
from handler_registry import HandlerRegistry
from task import Task
from task_result import TaskResult
from task_router import TaskRouter


class TaskExecutor:
    def __init__(
        self,
        task_router: TaskRouter,
        handler_registry: HandlerRegistry,
        event_system: EventSystem,
    ) -> None:
        self.task_router = task_router
        self.handler_registry = handler_registry
        self.event_system = event_system

    def execute(
        self,
        task: Task,
    ) -> TaskResult:
        self.event_system.emit(
            "task_execution_started",
            {
                "task_id": task.task_id,
                "task_type": task.task_type,
            },
        )

        handler_name = self.task_router.resolve_route(task.task_type)

        if handler_name is None:
            result = TaskResult(
                task_id=task.task_id,
                success=False,
                message=f"No route found for task type: {task.task_type}",
                error="missing_route",
            )

            self.event_system.emit(
                "task_execution_failed",
                {
                    "task_id": task.task_id,
                    "task_type": task.task_type,
                    "error": result.error,
                },
            )

            return result

        handler = self.handler_registry.get_handler(handler_name)

        if handler is None:
            result = TaskResult(
                task_id=task.task_id,
                success=False,
                message=f"No handler registered: {handler_name}",
                error="missing_handler",
            )

            self.event_system.emit(
                "task_execution_failed",
                {
                    "task_id": task.task_id,
                    "task_type": task.task_type,
                    "handler_name": handler_name,
                    "error": result.error,
                },
            )

            return result

        try:
            task.update_status("running")
            result = handler.handle(task)

            if result.success:
                task.update_status("completed")

                self.event_system.emit(
                    "task_execution_completed",
                    {
                        "task_id": task.task_id,
                        "task_type": task.task_type,
                        "handler_name": handler_name,
                    },
                )
            else:
                task.update_status("failed")

                self.event_system.emit(
                    "task_execution_failed",
                    {
                        "task_id": task.task_id,
                        "task_type": task.task_type,
                        "handler_name": handler_name,
                        "error": result.error,
                    },
                )

            return result

        except Exception as error:
            task.update_status("failed")

            result = TaskResult(
                task_id=task.task_id,
                success=False,
                message="Task execution failed.",
                error=str(error),
            )

            self.event_system.emit(
                "task_execution_failed",
                {
                    "task_id": task.task_id,
                    "task_type": task.task_type,
                    "handler_name": handler_name,
                    "error": result.error,
                },
            )

            return result