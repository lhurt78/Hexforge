from logger import (
    log_info,
    log_success,
    log_warning,
)


class TaskQueue:
    def __init__(self) -> None:
        self.tasks: list[dict] = []

    def add_task(
        self,
        task_name: str,
        payload: dict | None = None
    ) -> None:

        task = {
            "name": task_name,
            "payload": payload or {},
            "status": "queued",
        }

        self.tasks.append(task)

        log_info(f"Task queued: {task_name}")

    def process_next_task(self) -> dict | None:
        if not self.tasks:
            log_warning("No tasks in queue.")
            return None

        task = self.tasks.pop(0)

        task["status"] = "completed"

        log_success(
            f"Task processed: {task['name']}"
        )

        return task

    def get_queue_size(self) -> int:
        return len(self.tasks)

    def get_tasks(self) -> list[dict]:
        return self.tasks