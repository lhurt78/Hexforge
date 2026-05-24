from config_loader import load_environment_config
from environment import validate_python_version, validate_required_folders
from logger import log_info, log_success, log_error
from module_registry import ModuleRegistry
from memory_manager import MemoryManager
from knowledge_manager import KnowledgeManager
from research_manager import ResearchManager
from state_manager import StateManager


def run_startup_sequence() -> bool:
    log_info("Starting Hexforge bootstrap sequence...")

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
        log_error("Bootstrap validation failed.")
        return False

    log_success("Hexforge bootstrap completed successfully.")
    return True