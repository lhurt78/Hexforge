from handler_registry import HandlerRegistry
from task import Task
from task_result import TaskResult
from task_router import TaskRouter


class TaskExecutor:
    def __init__(
        self,
        task_router: TaskRouter,
        handler_registry: HandlerRegistry,
    ) -> None:
        self.task_router = task_router
        self.handler_registry = handler_registry

    def execute(
        self,
        task: Task,
    ) -> TaskResult:
        handler_name = self.task_router.resolve_route(task.task_type)

        if handler_name is None:
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message=f"No route found for task type: {task.task_type}",
                error="missing_route",
            )

        handler = self.handler_registry.get_handler(handler_name)

        if handler is None:
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message=f"No handler registered: {handler_name}",
                error="missing_handler",
            )

        try:
            task.update_status("running")
            result = handler.handle(task)

            if result.success:
                task.update_status("completed")
            else:
                task.update_status("failed")

            return result

        except Exception as error:
            task.update_status("failed")

            return TaskResult(
                task_id=task.task_id,
                success=False,
                message="Task execution failed.",
                error=str(error),
            )