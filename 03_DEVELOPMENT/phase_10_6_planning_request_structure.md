# Phase 10.6 - Planning Request Structure

---

# Purpose

Define the expected payload structure for `planning_task`.

This phase does not modify runtime code.

---

# Decision

Planning-specific fields belong inside `Task.payload`.

The core `Task` model remains generic.

---

# Required Payload Field

```python
"goal": str