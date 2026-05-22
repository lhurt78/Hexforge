# Hexforge Memory Architecture

# Purpose
This document defines how Hexforge stores, retrieves, summarizes, and organizes long-term project memory.

---

# MEMORY GOAL

Hexforge must remember projects across sessions without depending on a single endless conversation thread.

Memory must support:
- project continuity
- thread-to-thread recall
- decision tracking
- code/project history
- summaries
- user-approved context

---

# MEMORY TYPES

## 1. Session Memory
Temporary memory for the current conversation.

Stores:
- active prompt context
- recent user requests
- current task
- short-term reasoning context

This memory may expire after the session ends.

---

## 2. Thread Summary Memory
A condensed summary created before ending a thread.

Stores:
- what was discussed
- decisions made
- files changed
- current task status
- next recommended step

Thread summaries prevent long-context confusion.

---

## 3. Project Memory
Persistent memory tied to a specific project.

Stores:
- project goals
- project scope
- decisions
- architecture notes
- development history
- current status

---

## 4. Decision Memory
Permanent record of major project decisions.

Stores:
- decision
- date
- reason
- status
- related project

Major decisions should not be buried inside normal conversation logs.

---

## 5. Knowledge Memory
Information Hexforge has learned from approved sources.

Stores:
- topic
- source
- summary
- date learned
- reliability rating
- related project

---

# MEMORY STORAGE LOCATIONS

## Project Control
```text
00_PROJECT_CONTROL/