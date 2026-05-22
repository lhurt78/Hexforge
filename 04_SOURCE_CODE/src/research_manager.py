from logger import (
    log_info,
    log_success,
    log_warning,
)

from persistence_manager import (
    PersistenceManager
)

from constants import PROJECT_FOLDERS


class ResearchManager:
    def __init__(self) -> None:
        self.research_topics: list[dict] = []

        self.persistence = PersistenceManager()

        self.research_file = (
            PROJECT_FOLDERS["knowledge"]
            / "research_queue.json"
        )

    def add_research_topic(
        self,
        topic: str,
        source: str,
        priority: str = "normal"
    ) -> None:

        research_item = {
            "topic": topic,
            "source": source,
            "priority": priority,
            "status": "queued",
        }

        self.research_topics.append(
            research_item
        )

        log_info(
            f"Research topic queued: {topic}"
        )

    def complete_research(
        self,
        topic: str
    ) -> bool:

        for item in self.research_topics:
            if item["topic"] == topic:
                item["status"] = "completed"

                log_success(
                    f"Research completed: {topic}"
                )

                return True

        log_warning(
            f"Research topic not found: {topic}"
        )

        return False

    def save_research_queue(self) -> bool:
        return self.persistence.save_json(
            self.research_file,
            self.research_topics
        )

    def load_research_queue(self) -> bool:
        data = self.persistence.load_json(
            self.research_file
        )

        if data is None:
            return False

        self.research_topics = data

        log_success(
            "Research queue loaded."
        )

        return True

    def get_research_topics(self) -> list[dict]:
        return self.research_topics

    def get_research_count(self) -> int:
        return len(self.research_topics)