# Phase 8.6 - Task Handler Boundary

---

# Purpose

Define the ownership boundary for future Hexforge task handlers before implementation.

This phase does not implement handlers.

---

# Handler Definition

A task handler is a controlled unit of runtime logic responsible for one task type.

A handler should receive a task, perform one bounded operation, and return a structured task result.

---

# Handler Responsibilities

A future handler may:

* inspect a task
* validate required payload fields
* perform one specific operation
* return `TaskResult`
* report safe failure
* emit no events directly unless explicitly approved later

---

# Handler Restrictions

A handler must not:

* own routing
* register routes
* control unrelated managers
* bypass `TaskRouter`
* mutate global runtime state without authorization
* create hidden dependencies
* start background loops
* perform autonomous actions
* access protected systems without explicit injection
* act as a service container

---

# TaskRouter Boundary

`TaskRouter` remains responsible for:

* registering task type to handler name mappings
* resolving task type to handler name mappings
* emitting route lifecycle events

`TaskRouter` must not execute handlers.

---

# Future Executor Boundary

A future execution component may eventually:

* receive a `Task`
* ask `TaskRouter` for the appropriate handler
* invoke the handler
* receive a `TaskResult`
* emit execution lifecycle events

This executor should not be implemented until handler structure is defined.

---

# Event Rule

Handlers should not use events to command other systems.

Events may eventually be used to report execution state, but not to create hidden command chains.

---

# Phase 8.6 Decision

Task handlers should remain small, explicit, and bounded.

Handler implementation is deferred until a safe handler interface is defined.