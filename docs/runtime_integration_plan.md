# Hexforge Runtime Integration Plan

---

## Purpose

This document defines how Hexforge’s major systems connect during runtime.

Phase 4 focuses on integrating existing architecture into a coordinated runtime system without prematurely adding databases, embeddings, vector search, or live inference complexity.

---

## Runtime Startup Order

1. `startup.py`
2. `app_controller.py`
3. `service_manager.py`
4. `state_manager.py`
5. `persistence_manager.py`
6. `memory_manager.py`
7. `knowledge_manager.py`
8. `research_manager.py`
9. `model_manager.py`
10. `task_router.py`
11. `event_system.py`

---

## Central Runtime Coordinator

`app_controller.py` is the central runtime coordinator.

Its responsibilities are:

- Initialize the runtime
- Request services from `service_manager.py`
- Coordinate startup recovery
- Coordinate autosave readiness
- Prepare systems for task execution
- Handle clean shutdown later

---

## Service Manager Role

`service_manager.py` should remain responsible for registering, storing, and retrieving major subsystems.

It should not contain business logic.

Its job is service access, not service intelligence.

---

## State Manager Role

`state_manager.py` remains responsible for unified runtime state.

It should coordinate with:

- `persistence_manager.py`
- `memory_manager.py`
- `knowledge_manager.py`
- `research_manager.py`

The state manager should not replace those managers. It should track and coordinate their shared state.

---

## Persistence Manager Role

`persistence_manager.py` remains responsible for saving and loading JSON-backed persistent data.

It should not decide when autosave happens.

It should only perform the save/load work when asked.

---

## Cognitive Managers

The cognitive managers are:

- `memory_manager.py`
- `knowledge_manager.py`
- `research_manager.py`
- `model_manager.py`

These systems should eventually register themselves through the service manager.

They should avoid directly importing each other unless absolutely necessary.

---

## Task Router Role

`task_router.py` decides where tasks should go.

It should eventually receive access to registered services through the app controller or service manager.

It should not manually create its own manager instances.

---

## Event System Role

`event_system.py` should eventually broadcast important runtime events such as:

- startup complete
- recovery complete
- task received
- task completed
- autosave triggered
- shutdown requested

For now, this remains architecture planning only.

---

## Phase 4 Integration Rule

No new advanced features are added during initial runtime integration.

Do not add:

- database storage
- vector memory
- embeddings
- live inference
- autonomous execution
- internet research automation
- GUI logic

Phase 4 first connects the systems that already exist.

---

## Phase 4.1 Completion Criteria

Phase 4.1 is complete when:

- This runtime integration plan exists
- Runtime startup order is documented
- System responsibility boundaries are documented
- The next coding task is clearly defined