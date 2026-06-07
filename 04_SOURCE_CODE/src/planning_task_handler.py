from task import Task
from task_handler import TaskHandler
from task_result import TaskResult


class PlanningTaskHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        goal = task.payload.get("goal")

        if not goal:
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message="Planning task requires a goal.",
                error="missing_goal",
            )

        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Planning task completed.",
            data={
                "goal": goal,
                "recommended_steps": [
                    "Clarify the intended outcome.",
                    "Identify required resources.",
                    "Break the goal into smaller tasks.",
                    "Prioritize the first executable step.",
                    "Validate progress before expanding scope.",
                ],
            },
        )