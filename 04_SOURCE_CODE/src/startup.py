from config_loader import load_environment_config
from environment import validate_python_version, validate_required_folders
from logger import log_info, log_success, log_error
from module_registry import ModuleRegistry
from memory_manager import MemoryManager
from knowledge_manager import KnowledgeManager
from research_manager import ResearchManager
from state_manager import StateManager
from event_system import EventSystem
from runtime_events import (
    on_startup_begin,
    on_startup_complete,
    on_startup_failed,
    on_state_loaded,
    on_state_save_started,
    on_state_save_complete,
    on_state_save_failed,
    on_state_snapshot_started,
    on_state_snapshot_complete,
    on_state_snapshot_failed,
)

def run_startup_sequence() -> bool:
    log_info("Starting Hexforge bootstrap sequence...")

    event_system = EventSystem()

    event_system.subscribe(
        "startup_begin",
        on_startup_begin,
    )

    event_system.subscribe(
        "startup_complete",
        on_startup_complete,
    )

    event_system.subscribe(
        "startup_failed",
        on_startup_failed,
    )

    event_system.subscribe(
        "state_loaded",
        on_state_loaded,
    )
    
    event_system.subscribe(
        "state_save_started",
        on_state_save_started,
    )

    event_system.subscribe(
        "state_save_complete",
        on_state_save_complete,
    )

    event_system.subscribe(
        "state_save_failed",
        on_state_save_failed,
    )

    event_system.subscribe(
        "state_snapshot_started",
        on_state_snapshot_started,
    )

    event_system.subscribe(
        "state_snapshot_complete",
        on_state_snapshot_complete,
    )

    event_system.subscribe(
        "state_snapshot_failed",
        on_state_snapshot_failed,
    )

    registered_events = (
        event_system.get_registered_events()
    )

    for event_name in registered_events:
        listener_count = (
            event_system.get_listener_count(
                event_name
            )
        )

        log_info(
            f"Registered Event -> "
            f"{event_name} "
            f"({listener_count} listeners)"
        )

    event_system.emit(
        "startup_begin",
        {
            "status": "starting"
        }
    )

    load_environment_config()

    python_ok = validate_python_version()
    folders_ok = validate_required_folders()

    registry = ModuleRegistry()
    registry.register("memory_system", "planned")
    registry.register("knowledge_system", "planned")
    registry.register("research_system", "planned")
    registry.register("testing_system", "planned")
    registry.validate_registry()

    memory_manager = MemoryManager()
    knowledge_manager = KnowledgeManager()
    research_manager = ResearchManager()

    state_manager = StateManager(
        memory_manager=memory_manager,
        knowledge_manager=knowledge_manager,
        research_manager=research_manager,
        event_system=event_system,
    )

    state_manager.load_all_state()

    summary = state_manager.get_state_summary()

    log_info(
        f"Recovered State -> "
        f"Memory: {summary['memory_count']} | "
        f"Knowledge: {summary['knowledge_count']} | "
        f"Research: {summary['research_count']}"
    )

    if not python_ok or not folders_ok:
        event_system.emit(
            "startup_failed",
            {
                "status": "failed"
            }
        )

        log_error("Bootstrap validation failed.")
        return False

    event_system.emit(
        "startup_complete",
        {
            "status": "ready"
        }
    )

    log_success("Hexforge bootstrap completed successfully.")
    return True