import re

from task import Task
from task_handler import TaskHandler
from task_result import TaskResult


class PlanningTaskHandler(TaskHandler):
    def handle(
        self,
        task: Task,
    ) -> TaskResult:
        validation_error = self._validate_payload(task.payload)

        if validation_error is not None:
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message=validation_error["message"],
                error=validation_error["error"],
            )

        goal = task.payload["goal"].strip()
        scope = self._clean_optional_string(
            task.payload.get("scope")
        )
        constraints = self._clean_constraints(
            task.payload.get("constraints", [])
        )
        priority = self._clean_optional_string(
            task.payload.get("priority")
        )
        target_outcome = self._clean_optional_string(
            task.payload.get("target_outcome")
        )

        category = self._determine_category(goal)
        recommended_steps = self._get_recommended_steps(category)
        planning_notes = self._build_planning_notes(
            scope=scope,
            constraints=constraints,
            priority=priority,
            target_outcome=target_outcome,
        )

        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Planning task completed.",
            data={
                "goal": goal,
                "category": category,
                "scope": scope,
                "constraints": constraints,
                "priority": priority,
                "target_outcome": target_outcome,
                "recommended_steps": recommended_steps,
                "planning_notes": planning_notes,
            },
        )

    def _validate_payload(
        self,
        payload: dict,
    ) -> dict | None:
        goal = payload.get("goal")

        if not isinstance(goal, str) or not goal.strip():
            return {
                "message": "Planning task requires a goal.",
                "error": "missing_goal",
            }

        scope = payload.get("scope")

        if scope is not None and not isinstance(scope, str):
            return {
                "message": "Planning task scope must be a string.",
                "error": "invalid_scope",
            }

        constraints = payload.get("constraints")

        if constraints is not None:
            if not isinstance(constraints, list):
                return {
                    "message": "Planning task constraints must be a list.",
                    "error": "invalid_constraints",
                }

            for constraint in constraints:
                if (
                    not isinstance(constraint, str)
                    or not constraint.strip()
                ):
                    return {
                        "message": (
                            "Planning task constraints must contain "
                            "non-empty strings."
                        ),
                        "error": "invalid_constraints",
                    }

        priority = payload.get("priority")

        if priority is not None and not isinstance(priority, str):
            return {
                "message": "Planning task priority must be a string.",
                "error": "invalid_priority",
            }

        target_outcome = payload.get("target_outcome")

        if (
            target_outcome is not None
            and not isinstance(target_outcome, str)
        ):
            return {
                "message": (
                    "Planning task target_outcome must be a string."
                ),
                "error": "invalid_target_outcome",
            }

        return None

    def _clean_optional_string(
        self,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        return value.strip()

    def _clean_constraints(
        self,
        constraints: list[str],
    ) -> list[str]:
        return [
            constraint.strip()
            for constraint in constraints
        ]

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

    def _build_planning_notes(
        self,
        scope: str | None,
        constraints: list[str],
        priority: str | None,
        target_outcome: str | None,
    ) -> list[str]:
        notes = []

        if scope:
            notes.append(
                f"Scope defined: {scope}"
            )

        if constraints:
            notes.append(
                "Constraints must shape the first executable plan."
            )

        if priority:
            notes.append(
                f"Priority level: {priority}"
            )

        if target_outcome:
            notes.append(
                f"Target outcome: {target_outcome}"
            )

        if not notes:
            notes.append(
                "No optional planning details were provided."
            )

        return notes