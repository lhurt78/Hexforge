from logger import (
    log_info,
    log_success,
    log_warning,
)

from persistence_manager import (
    PersistenceManager
)

from constants import PROJECT_FOLDERS


class KnowledgeManager:
    def __init__(self) -> None:
        self.knowledge_base: dict[str, dict] = {}

        self.persistence = PersistenceManager()

        self.knowledge_file = (
            PROJECT_FOLDERS["knowledge"]
            / "knowledge_store.json"
        )

    def add_knowledge(
        self,
        topic: str,
        content: str,
        source: str
    ) -> None:

        self.knowledge_base[topic] = {
            "content": content,
            "source": source,
        }

        log_info(f"Knowledge added: {topic}")

    def get_knowledge(
        self,
        topic: str
    ) -> dict | None:

        knowledge = self.knowledge_base.get(topic)

        if knowledge is None:
            log_warning(
                f"Knowledge not found: {topic}"
            )
            return None

        log_success(
            f"Knowledge retrieved: {topic}"
        )

        return knowledge

    def remove_knowledge(
        self,
        topic: str
    ) -> bool:

        if topic not in self.knowledge_base:
            log_warning(
                f"Cannot remove missing topic: {topic}"
            )
            return False

        del self.knowledge_base[topic]

        log_success(
            f"Knowledge removed: {topic}"
        )

        return True

    def save_knowledge(self) -> bool:
        return self.persistence.save_json(
            self.knowledge_file,
            self.knowledge_base
        )

    def load_knowledge(self) -> bool:
        data = self.persistence.load_json(
            self.knowledge_file
        )

        if data is None:
            return False

        self.knowledge_base = data

        log_success(
            "Knowledge store loaded."
        )

        return True

    def get_knowledge_count(self) -> int:
        return len(self.knowledge_base)