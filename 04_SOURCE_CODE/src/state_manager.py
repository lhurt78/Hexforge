from datetime import datetime
from pathlib import Path
from event_system import EventSystem

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

from constants import (
    PROJECT_FOLDERS
)


class StateManager:
    def __init__(
        self,
        memory_manager: MemoryManager,
        knowledge_manager: KnowledgeManager,
        research_manager: ResearchManager,
        event_system: EventSystem,
    ) -> None:
        self.memory_manager = memory_manager
        self.knowledge_manager = knowledge_manager
        self.research_manager = research_manager
        self.event_system = event_system

    def save_all_state(self) -> bool:
        log_info("Saving all system state...")

        self.event_system.emit(
            "state_save_started",
            {}
        )

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
            self.event_system.emit(
                "state_save_complete",
                {}
            )

            log_success(
                "All state saved successfully."
            )

            if not success:
                self.event_system.emit(
                    "state_save_failed",
                    {}
            )

        return success

    def autosave_state(self) -> bool:
        log_info("Autosaving system state...")

        success = self.save_all_state()

        if success:
            log_success("Autosave completed successfully.")

        return success
    
    def load_all_state(self) -> bool:
        log_info("Loading all system state...")

        self.memory_manager.load_memories()

        self.knowledge_manager.load_knowledge()

        self.research_manager.load_research_queue()

        log_success(
            "All available state loaded."
        )

        self.event_system.emit(
            "state_loaded",
            self.get_state_summary(),
        )

        return True

    def get_state_summary(self) -> dict:
        return {
            "memory_count": (
                self.memory_manager
                .get_memory_count()
            ),
            "knowledge_count": (
                self.knowledge_manager
                .get_knowledge_count()
            ),
            "research_count": (
                self.research_manager
                .get_research_count()
            ),
        }

    def create_state_snapshot(self) -> bool:
        self.event_system.emit(
            "state_snapshot_started",
            {}
        )
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        snapshot_dir = (
            PROJECT_FOLDERS["backups"]
            / "snapshots"
            / f"state_snapshot_{timestamp}"
        )

        snapshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        memory_saved = (
            self.memory_manager
            .persistence
            .save_json(
                snapshot_dir / "memory_store.json",
                self.memory_manager.memories
            )
        )

        knowledge_saved = (
            self.knowledge_manager
            .persistence
            .save_json(
                snapshot_dir / "knowledge_store.json",
                self.knowledge_manager.knowledge_base
            )
        )

        research_saved = (
            self.research_manager
            .persistence
            .save_json(
                snapshot_dir / "research_queue.json",
                self.research_manager.research_topics
            )
        )

        success = all([
            memory_saved,
            knowledge_saved,
            research_saved,
        ])

        if success:
            self.event_system.emit(
                "state_snapshot_complete",
                {
                    "snapshot_path": str(snapshot_dir)
                }
            )

            log_success(
                f"State snapshot created: "
                f"{snapshot_dir}"
            )

        if not success:
            self.event_system.emit(
                "state_snapshot_failed",
                {
                    "snapshot_path": str(snapshot_dir)
                }
            )

        return success
    
    def restore_state_snapshot(
        self,
        snapshot_path: Path
    ) -> bool:

        log_info(
            f"Restoring snapshot: {snapshot_path}"
        )

        self.event_system.emit(
            "state_restore_started",
            {
                "snapshot_path": str(snapshot_path)
            }
        )

        memory_data = (
            self.memory_manager
            .persistence
            .load_json(
                snapshot_path / "memory_store.json"
            )
        )

        knowledge_data = (
            self.knowledge_manager
            .persistence
            .load_json(
                snapshot_path / "knowledge_store.json"
            )
        )

        research_data = (
            self.research_manager
            .persistence
            .load_json(
                snapshot_path / "research_queue.json"
            )
        )

        restore_success = any([
            memory_data is not None,
            knowledge_data is not None,
            research_data is not None,
        ])

        if not restore_success:
            self.event_system.emit(
                "state_restore_failed",
                {
                    "snapshot_path": str(snapshot_path)
                }
            )

            return False

        if memory_data is not None:
            self.memory_manager.memories = (
                memory_data
            )

        if knowledge_data is not None:
            self.knowledge_manager.knowledge_base = (
                knowledge_data
            )

        if research_data is not None:
            self.research_manager.research_topics = (
                research_data
            )

        self.event_system.emit(
            "state_restore_complete",
            {
                "snapshot_path": str(snapshot_path)
            }
        )

        log_success(
            "Snapshot restored successfully."
        )

        return True