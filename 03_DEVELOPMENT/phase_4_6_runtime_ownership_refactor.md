# Phase 4.6 - Runtime Ownership Refactor

## Purpose

Clarify runtime ownership boundaries without changing stable runtime behavior unnecessarily.

---

## Refactor Decision

No persistence ownership refactor will be performed during Phase 4.6.

Current manager-owned persistence remains in place.

---

## Runtime Ownership Boundary

```txt
startup.py
    owns runtime assembly

StateManager
    owns runtime state coordination

MemoryManager
KnowledgeManager
ResearchManager
    own domain-specific data and persistence

ServiceManager
    owns service status tracking only