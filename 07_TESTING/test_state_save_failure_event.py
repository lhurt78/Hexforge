import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "04_SOURCE_CODE" / "src"

sys.path.append(str(SOURCE_PATH))

from event_system import EventSystem
from state_manager import StateManager


class FakeMemoryManager:
    def save_memories(self):
        return False


class FakeKnowledgeManager:
    def save_knowledge(self):
        return True


class FakeResearchManager:
    def save_research_queue(self):
        return True


events_seen = []


def on_save_failed(data: dict) -> None:
    events_seen.append("state_save_failed")


event_system = EventSystem()

event_system.subscribe(
    "state_save_failed",
    on_save_failed,
)

state_manager = StateManager(
    memory_manager=FakeMemoryManager(),
    knowledge_manager=FakeKnowledgeManager(),
    research_manager=FakeResearchManager(),
    event_system=event_system,
)

result = state_manager.save_all_state()

print("Save result:", result)
print("Events seen:", events_seen)

expected_events = [
    "state_save_failed",
]

if (
    result is False
    and events_seen == expected_events
):
    print(
        "State save failure event validation passed."
    )
else:
    print(
        "State save failure event validation failed."
    )
    raise SystemExit(1)