from logger import (
    log_info,
    log_success,
)

from memory_manager import (
    MemoryManager
)

from knowledge_manager import (
    KnowledgeManager
)

from research_manager import (
    ResearchManager
)


class StateManager:
    def __init__(self) -> None:
        self.memory_manager = MemoryManager()
        self.knowledge_manager = KnowledgeManager()
        self.research_manager = ResearchManager()

    def save_all_state(self) -> bool:
        log_info("Saving all system state...")

        memory_saved = (
            self.memory_manager.save_memories()
        )

        knowledge_saved = (
            self.knowledge_manager.save_knowledge()
        )

        research_saved = (
            self.research_manager
            .save_research_queue()
        )

        success = all([
            memory_saved,
            knowledge_saved,
            research_saved,
        ])

        if success:
            log_success(
                "All state saved successfully."
            )

        return success

    def load_all_state(self) -> bool:
        log_info("Loading all system state...")

        self.memory_manager.load_memories()

        self.knowledge_manager.load_knowledge()

        self.research_manager.load_research_queue()

        log_success(
            "All available state loaded."
        )

        return True
    
    def get_state_summary(self) -> dict:
        return {
            "memory_count": self.memory_manager.get_memory_count(),
            "knowledge_count": self.knowledge_manager.get_knowledge_count(),
            "research_count": self.research_manager.get_research_count(),
        }