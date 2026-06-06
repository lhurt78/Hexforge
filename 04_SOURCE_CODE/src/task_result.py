from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TaskResult:
    task_id: str
    success: bool
    message: str
    data: dict = field(default_factory=dict)
    error: str | None = None
    completed_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )