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

        overview = self._build_overview(
            goal=goal,
            category=category,
        )

        constraints_summary = self._build_constraints_summary(
            constraints=constraints
        )

        risks = self._build_risks(
            constraints=constraints,
            scope=scope,
            target_outcome=target_outcome,
        )

        success_criteria = self._build_success_criteria(
            scope=scope,
            target_outcome=target_outcome,
        )

        planning_assumptions = self._build_planning_assumptions(
            scope=scope,
            constraints=constraints,
            priority=priority,
            target_outcome=target_outcome,
        )

        next_action = (
            recommended_steps[0]
            if recommended_steps
            else None
        )

        return TaskResult(
            task_id=task.task_id,
            success=True,
            message="Planning task completed.",
            data={
                "overview": overview,

                "goal": goal,
                "category": category,

                "scope": scope,
                "constraints": constraints,
                "priority": priority,
                "target_outcome": target_outcome,

                "recommended_steps": recommended_steps,

                "constraints_summary": constraints_summary,
                "risks": risks,
                "next_action": next_action,

                "success_criteria": success_criteria,
                "planning_assumptions": planning_assumptions,
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

    def _build_overview(
        self,
        goal: str,
        category: str,
    ) -> str:
        return (
            f"{category.title()} planning request identified: {goal}"
        )

    def _build_constraints_summary(
        self,
        constraints: list[str],
    ) -> str:
        if not constraints:
            return "No constraints specified."

        return (
            f"{len(constraints)} constraints specified."
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
                "Scope should be used to limit the planning response."
            )

        if constraints:
            notes.append(
                "Constraints should be reviewed before execution begins."
            )

        if priority:
            notes.append(
                "Priority should influence which step is handled first."
            )

        if target_outcome:
            notes.append(
                "Target outcome should be used to verify completion."
            )

        if not notes:
            notes.append(
                "No supplemental planning notes were generated."
            )

        return notes

    def _build_risks(
        self,
        constraints: list[str],
        scope: str | None,
        target_outcome: str | None,
    ) -> list[str]:
        risks = []

        if constraints:
            risks.append(
                "Defined constraints may limit available execution options."
            )
        else:
            risks.append(
                "Missing constraints may allow uncontrolled scope expansion."
            )

        if scope is None:
            risks.append(
                "Missing scope may cause planning drift."
            )

        if target_outcome is None:
            risks.append(
                "Missing target outcome may make completion harder to verify."
            )

        return risks

    def _build_success_criteria(
        self,
        scope: str | None,
        target_outcome: str | None,
    ) -> list[str]:
        criteria = [
            "The planning goal is clearly documented.",
            "Recommended execution steps are available.",
        ]

        if scope:
            criteria.append(
                "Project scope is defined well enough to guide planning."
            )

        if target_outcome:
            criteria.append(
                "Target outcome is defined well enough to verify completion."
            )

        return criteria

    def _build_planning_assumptions(
        self,
        scope: str | None,
        constraints: list[str],
        priority: str | None,
        target_outcome: str | None,
    ) -> list[str]:
        assumptions = []

        if scope is None:
            assumptions.append(
                "No project scope was provided."
            )

        if not constraints:
            assumptions.append(
                "No project constraints were provided."
            )

        if priority is None:
            assumptions.append(
                "No project priority was provided."
            )

        if target_outcome is None:
            assumptions.append(
                "No target outcome was provided."
            )

        return assumptions