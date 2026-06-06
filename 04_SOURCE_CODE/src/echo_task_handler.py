from task import Task
from task_handler import TaskHandler
from task_result import TaskResult


class EchoTaskHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Echo task completed.",
            data={
                "task_type": task.task_type,
                "payload": task.payload,
                "source": task.source,
                "metadata": task.metadata,
            },
        )