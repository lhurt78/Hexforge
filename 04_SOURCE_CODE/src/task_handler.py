from abc import ABC, abstractmethod

from task import Task
from task_result import TaskResult


class TaskHandler(ABC):
    @abstractmethod
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        pass