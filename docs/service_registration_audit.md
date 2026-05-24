# Hexforge Service Registration Audit

---

## Purpose

This document audits how Hexforge services are currently instantiated, registered, and accessed during runtime.

The goal is to identify architectural problems before runtime integration expands further.

---

## Project Structure Clarification

Hexforge currently does not use a `src/core/` subdirectory structure.

All primary runtime and manager files currently exist directly inside:

`src/`

Examples:

- `src/service_manager.py`
- `src/app_controller.py`
- `src/state_manager.py`

Future architectural restructuring may introduce subfolders later, but Phase 4 currently operates under a flat `src/` structure.

---

## Current Service Registration Status

| System | Registered | Notes |
|---|---|---|
| app_controller | YES | Central runtime coordinator |
| service_manager | YES | Handles service registration and retrieval |
| state_manager | YES | Unified runtime state coordinator |
| persistence_manager | YES | JSON persistence layer |
| memory_manager | YES | Cognitive memory system |
| knowledge_manager | YES | Knowledge storage system |
| research_manager | YES | Research tracking system |
| model_manager | YES | Model abstraction layer |
| task_router | YES | Task routing system |
| event_system | YES | Runtime event broadcasting |

---

## Direct Manager Instantiation Audit

- `state_manager.py`
  - manually creates:
    - `MemoryManager`
    - `KnowledgeManager`
    - `ResearchManager`

Current implementation:

```python
self.memory_manager = MemoryManager()
self.knowledge_manager = KnowledgeManager()
self.research_manager = ResearchManager()
```

This is currently the only identified direct manager instantiation pattern.

This is considered a temporary acceptable violation during Phase 4 until service registration integration is completed.

---

## Circular Dependency Risks

Current circular dependency risk appears LOW.

No major recursive manager import chains were identified during the Phase 4.2 audit.

Most systems currently maintain relatively clean responsibility separation.

---

## Runtime Ownership Audit

| Runtime Responsibility | Current Owner |
|---|---|
| startup flow | `startup.py` |
| runtime coordination | `app_controller.py` |
| service registration | `service_manager.py` |
| unified runtime state | `state_manager.py` |
| persistence operations | `persistence_manager.py` |
| task routing | `task_router.py` |
| event broadcasting | `event_system.py` |
| autosave triggering | `state_manager.py` |
| recovery logic | `startup.py` + `state_manager.py` |

---

## Temporary Acceptable Violations

The following temporary architectural violations are currently acceptable during Phase 4 integration:

- `state_manager.py` directly instantiates cognitive managers
- Flat `src/` structure instead of segmented architecture folders
- Limited direct manager imports where runtime integration is incomplete

These may later be replaced with dependency injection or centralized service retrieval.

---

## Phase 4.2 Findings

- Architecture remains relatively clean
- Minimal direct manager instantiation detected
- No major circular dependency patterns identified
- Runtime ownership remains mostly centralized
- Current primary integration concern:
  - `state_manager.py` manually instantiates cognitive managers
- Overall architectural stability currently rated:
  - LOW RISK

---

## Phase 4.2 Completion Criteria

Phase 4.2 is complete when:

- All major systems are audited
- Manual manager creation points are identified
- Circular dependency risks are documented
- Runtime ownership is documented
- Next integration refactor targets are known