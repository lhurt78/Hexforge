from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


VALID_TASK_STATUSES = {
    "created",
    "routed",
    "running",
    "completed",
    "failed",
}


@dataclass
class Task:
    task_type: str
    payload: dict
    source: str = "user"
    metadata: dict = field(default_factory=dict)
    task_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    status: str = "created"
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    def update_status(self, status: str) -> bool:
        if status not in VALID_TASK_STATUSES:
            return False

        self.status = status
        return True