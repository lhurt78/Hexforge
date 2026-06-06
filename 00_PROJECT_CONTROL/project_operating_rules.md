# Hexforge Project Operating Rules

---

# Document Purpose

This document is the long-term project governance and handoff reference for Hexforge.

It is not a progress note.

It defines:

* what Hexforge is
* what Hexforge is intended to become
* how Hexforge must be developed
* what architectural rules must remain consistent between threads
* how future development threads should operate

This document should change rarely.

---

# Project Identity

## Project Name

Hexforge

## Project Type

Local AI-assisted production platform

## Primary Purpose

Hexforge is being built as a controlled local AI system for creative and technical production work.

Its intended long-term purpose is to assist with:

* software development
* game development
* film production
* writing
* research
* planning
* project organization
* creative production workflows

## What Hexforge Is Not

Hexforge is not intended to be:

* unrestricted AGI
* an uncontrolled autonomous internet agent
* a self-modifying AI system
* a general-purpose unsupervised automation engine
* a system that acts outside defined scope boundaries

Hexforge must remain controlled, modular, inspectable, and purpose-driven.

---

# Development Success Criteria

## Short-Term Goal

Build a stable runtime foundation capable of:

* state management
* event coordination
* controlled task routing
* runtime service coordination
* project persistence

## Mid-Term Goal

Build production systems capable of:

* project planning
* research assistance
* software development assistance
* game development assistance
* writing assistance
* film production assistance

## Long-Term Goal

Create a controlled local production AI platform capable of coordinating complex creative and technical projects while remaining:

* modular
* inspectable
* maintainable
* extensible
* safe

---

# Development Priority Order

When conflicts occur, prioritize:

1. Runtime stability
2. Architecture integrity
3. Maintainability
4. Production progress
5. New features
6. Convenience

---

# Development Philosophy

Hexforge development must follow these principles:

* controlled expansion
* small validated production steps
* modular architecture
* explicit ownership boundaries
* no premature complexity
* no broad refactors without verification
* production movement must not be replaced by endless planning
* verification must support implementation, not stall it
* foundation stability takes priority over advanced features

---

# Phase Development Strategy

Hexforge development follows a staged progression.

## Phase 0

Preproduction Reconstruction

## Phase 1

Environment and Startup Foundation

## Phase 2

Core Runtime Architecture

## Phase 3

Persistent Cognitive Systems

## Phase 4

Runtime Integration

## Phase 5

Runtime Coordination Planning

## Phase 6

Controlled Runtime Expansion

## Phase 7+

Runtime Coordination Expansion

Future phases should expand capability incrementally while preserving verified ownership boundaries.

---

# Verified Architecture Principles

The following architecture facts are currently authoritative:

* `main.py` owns top-level application entry
* `main.py` handles startup failure and unhandled startup exceptions
* `startup.py` owns runtime assembly
* `startup.py` creates runtime dependencies
* `startup.py` registers runtime event listeners
* `startup.py` injects dependencies into runtime systems
* `StateManager` owns runtime state coordination
* `StateManager` receives dependencies through explicit injection
* `EventSystem` owns runtime event dispatch
* `runtime_events.py` owns runtime event listener functions
* `ModuleRegistry` handles static registration metadata only
* `ServiceManager` is not a dependency container
* persistence ownership remains decentralized
* async execution remains deferred
* `RuntimeContext` remains conceptual unless explicitly implemented in a later phase

---

# Architecture Change Protection

The following verified architecture decisions must not be altered without explicit verification and justification:

* `startup.py` owns runtime assembly
* `EventSystem` owns runtime event dispatch
* `StateManager` owns runtime state coordination
* `ModuleRegistry` remains metadata-only unless intentionally redesigned
* `ServiceManager` remains non-container unless intentionally redesigned
* persistence remains decentralized unless intentionally redesigned

Future threads should treat these decisions as protected architecture until formally changed.

---

# Runtime Command

The verified runtime command is:

```bash
python 04_SOURCE_CODE\src\main.py
```

---

# Physical Runtime Source Location

Runtime source code is located under:

```txt
04_SOURCE_CODE/src/
```

There is no assumed root-level `src` folder.

---

# Development Workflow Rules

## No-Assumption Rule

Never assume:

* file contents
* folder structure
* imports
* dependency ownership
* startup flow
* runtime flow
* persistence behavior
* manager ownership
* event behavior
* task routing behavior

Runtime-critical assumptions must be verified directly from uploaded or provided source files.

---

# Targeted Verification Rule

Verify only files directly related to the active task.

Avoid broad re-verification of previously verified and unchanged files.

Verification exists to support implementation, not replace implementation.

If a file has already been verified and has not changed, it should not be re-verified unless:

* it is directly involved in the current task
* a runtime error points to it
* a dependency change affects it
* the user specifically requests re-verification

---

# File Modification Rules

All future file modification instructions must include:

* exact physical file path
* exact insertion location
* exact action
* whether runtime validation is required

Avoid vague instructions such as:

* “add this somewhere”
* “wire this in”
* “update the manager”

Instructions must be specific enough for safe manual implementation.

---

# Runtime Validation Rules

Runtime validation is required after:

* import changes
* constructor changes
* dependency injection changes
* startup flow changes
* persistence logic changes
* filesystem behavior changes
* manager ownership changes
* runtime orchestration changes
* async/event system changes
* actual runtime-affecting code changes

Runtime validation is usually not required after:

* documentation-only phases
* planning-only phases
* status updates
* architecture mapping
* comments-only changes
* docstrings-only changes

---

# Manual Validation Format

When manual validation is required outside normal startup, instructions must include:

1. exact command to enter test mode
2. exact code to paste
3. expected result
4. exact command to exit test mode

Example exit command:

```python
exit()
```

---

# Commit Workflow

Preferred rhythm:

```txt
small change
validate
commit
push
continue
```

Standard commit workflow:

```bash
git status
git add .
git commit -m "Clear phase-based commit message"
git push
```

---

# Thread Handoff Requirements

Every new Hexforge development thread must begin by uploading:

```txt
00_PROJECT_CONTROL/project_operating_rules.md
00_PROJECT_CONTROL/current_status.md
```

Then upload all active source files required for the current phase.

---

# Required New Thread Behavior

At the start of a new thread:

1. Read `project_operating_rules.md`
2. Read `current_status.md`
3. Treat both documents as authoritative
4. Request active phase files if not already provided
5. Verify only files directly related to the current task
6. Do not begin modifications until required files are available
7. Avoid broad re-verification loops
8. Continue from the current phase/task listed in `current_status.md`

---

# Documentation Responsibilities

## `project_operating_rules.md`

This document answers:

```txt
What is Hexforge?
Why is Hexforge being built?
How must Hexforge be developed?
What rules govern development?
What architecture decisions are currently authoritative?
```

This file changes rarely.

## `current_status.md`

This document answers:

```txt
Where is Hexforge right now?
What was completed?
What is next?
Which files are active?
What must be uploaded next thread?
```

This file changes during:

* checkpoints
* thread switches
* end-of-day updates
* major milestones

---

# Project Handoff System

Hexforge now uses a two-document handoff model:

```txt
project_operating_rules.md
    = Project Constitution

current_status.md
    = Project Status Snapshot
```

Together these documents provide the complete project handoff state between development threads.
