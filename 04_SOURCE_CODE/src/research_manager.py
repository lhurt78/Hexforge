from logger import (
    log_info,
    log_success,
    log_warning,
)


class ResearchManager:
    def __init__(self) -> None:
        self.research_topics: list[dict] = []

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

    def get_research_topics(self) -> list[dict]:
        return self.research_topics

    def get_research_count(self) -> int:
        return len(self.research_topics)