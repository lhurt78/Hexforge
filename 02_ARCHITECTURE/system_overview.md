# Hexforge System Overview

# Purpose
This document describes the overall structure and operational philosophy of Hexforge.

---

# CORE SYSTEM DESIGN

Hexforge is built as a modular local-first AI assistant platform.

The system is divided into separate subsystems responsible for:
- conversation
- memory
- research
- file handling
- coding assistance
- workflow management
- tool integrations

Each subsystem should remain modular and independently replaceable.

---

# PRIMARY SYSTEMS

## 1. Conversation System

### Responsibilities
- User interaction
- Prompt handling
- Response formatting
- Session tracking
- Thread management

### Important Rules
- Keep responses structured
- Maintain project focus
- Warn when threads become too large
- Generate summaries before thread transitions

---

## 2. Memory System

### Responsibilities
- Store project summaries
- Store decisions
- Maintain thread continuity
- Recall past projects
- Organize persistent context

### Important Rules
- Memory must remain organized
- Information must be searchable
- Summaries should remain concise
- User approval required for critical memory updates

---

## 3. Research System

### Responsibilities
- Retrieve approved information
- Verify source safety
- Filter blocked domains
- Generate research summaries

### Important Rules
- Approved sources only
- Block untrusted domains
- Log research activity
- Never autonomously expand permissions

---

## 4. File Management System

### Responsibilities
- Read project files
- Write approved changes
- Organize project folders
- Create backups
- Track modifications

### Important Rules
- Never overwrite critical data without backup
- Track changes
- Restrict dangerous file operations

---

## 5. Coding Assistance System

### Responsibilities
- Explain code
- Generate code snippets
- Analyze bugs
- Assist project development

### Important Rules
- Maintain readability
- Favor modular code
- Prioritize maintainability
- Avoid unnecessary complexity

---

## 6. Workflow Management System

### Responsibilities
- Guide project planning
- Generate checklists
- Manage production workflows
- Track progress

### Important Rules
- Focus on structured planning
- Prevent scope creep
- Require milestone completion before expansion

---

# LONG-TERM EXPANSION SYSTEMS

Future optional systems may include:
- Blender integration
- Unity integration
- Unreal integration
- Voice interaction
- Mobile companion app
- Visual avatar systems

These systems remain outside the initial development scope.

---

# SYSTEM COMMUNICATION PHILOSOPHY

All systems should communicate through:
- clearly defined interfaces
- structured data
- controlled permissions

No subsystem should operate without oversight from the core control systems.

---

# PRIMARY DEVELOPMENT PRINCIPLES

## Principle 1
Stability before expansion.

## Principle 2
Documentation before implementation.

## Principle 3
Testing before deployment.

## Principle 4
User authority above automation.

## Principle 5
Controlled modular growth.

---

# THREAD MANAGEMENT POLICY

When conversation context becomes:
- unstable
- repetitive
- excessively large
- unfocused

Hexforge should:
1. summarize the current session
2. update project memory
3. recommend a fresh thread