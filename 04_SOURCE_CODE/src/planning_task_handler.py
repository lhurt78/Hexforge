import re

from task import Task
from task_handler import TaskHandler
from task_result import TaskResult


class PlanningTaskHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        goal = task.payload.get("goal")

        if not isinstance(goal, str) or not goal.strip():
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message="Planning task requires a goal.",
                error="missing_goal",
            )

        clean_goal = goal.strip()
        category = self._determine_category(clean_goal)
        recommended_steps = self._get_recommended_steps(category)

        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Planning task completed.",
            data={
                "goal": clean_goal,
                "category": category,
                "recommended_steps": recommended_steps,
            },
        )

    def _determine_category(
        self,
        goal: str,
    ) -> str:
        normalized_goal = goal.lower()

        category_keywords = {
            "software": [
                "software",
                "program",
                "app",
                "code",
                "coding",
                "python",
                "script",
                "utility",
            ],
            "game": [
                "game",
                "prototype",
                "unity",
                "godot",
                "playable",
            ],
            "film": [
                "film",
                "short film",
                "movie",
                "scene",
                "production plan",
                "shoot",
            ],
            "writing": [
                "book",
                "story",
                "novel",
                "chapter",
                "writing",
                "draft",
            ],
        }

        for category, keywords in category_keywords.items():
            for keyword in keywords:
                pattern = rf"\b{re.escape(keyword)}\b"

                if re.search(pattern, normalized_goal):
                    return category

        return "general"

    def _get_recommended_steps(
        self,
        category: str,
    ) -> list[str]:
        category_steps = {
            "software": [
                "Define the core problem the software must solve.",
                "Identify required inputs, outputs, and user actions.",
                "Break the system into small runtime components.",
                "Implement the smallest testable feature first.",
                "Validate behavior before expanding functionality.",
            ],
            "game": [
                "Define the core player experience.",
                "Identify the minimum playable loop.",
                "List required prototype assets and systems.",
                "Build the smallest playable version first.",
                "Test whether the loop is fun before expanding scope.",
            ],
            "film": [
                "Define the central concept and intended audience reaction.",
                "Identify locations, cast, props, and production limits.",
                "Break the project into script, shoot, sound, and edit tasks.",
                "Plan the smallest shootable version first.",
                "Validate the idea with a rough cut before expanding.",
            ],
            "writing": [
                "Define the premise and intended reader experience.",
                "Identify the main character, conflict, and stakes.",
                "Break the work into outline, draft, revision, and polish stages.",
                "Write the smallest complete scene or section first.",
                "Review structure before expanding the draft.",
            ],
            "general": [
                "Clarify the intended outcome.",
                "Identify required resources.",
                "Break the goal into smaller tasks.",
                "Prioritize the first executable step.",
                "Validate progress before expanding scope.",
            ],
        }

        return category_steps.get(
            category,
            category_steps["general"],
        )