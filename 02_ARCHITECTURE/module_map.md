# Hexforge Module Map

# Purpose
This document tracks the major systems, modules, and responsibilities inside Hexforge.

---

# CORE PROJECT STRUCTURE

## main.py
Primary program entry point.

Responsibilities:
- initialize systems
- start application
- manage startup sequence

---

# CONFIGURATION SYSTEM

## config_manager.py

Responsibilities:
- load configuration settings
- manage environment variables
- validate configuration data

---

# CONVERSATION SYSTEM

## conversation_manager.py

Responsibilities:
- manage chat sessions
- process prompts
- manage thread handling
- create session summaries

---

# MEMORY SYSTEM

## memory_manager.py

Responsibilities:
- store summaries
- retrieve project history
- organize persistent memory

---

## summary_manager.py

Responsibilities:
- create thread summaries
- condense project discussions
- prepare thread transition reports

---

# RESEARCH SYSTEM

## research_manager.py

Responsibilities:
- process research requests
- filter sources
- organize research results

---

## source_validator.py

Responsibilities:
- approve or reject URLs
- manage whitelist
- manage blocked domains

---

# FILE SYSTEM

## file_manager.py

Responsibilities:
- read files
- write files
- manage backups
- organize project directories

---

# CODING SYSTEM

## code_assistant.py

Responsibilities:
- explain code
- generate snippets
- analyze errors
- assist development

---

# WORKFLOW SYSTEM

## workflow_manager.py

Responsibilities:
- project planning
- milestone tracking
- production workflow generation

---

# LOGGING SYSTEM

## logger_manager.py

Responsibilities:
- log events
- track errors
- record system actions

---

# FUTURE MODULES

## blender_integration.py
Future Blender support.

## unity_integration.py
Future Unity support.

## unreal_integration.py
Future Unreal Engine support.

---

# MODULE DESIGN RULES

## Rule 1
Each module should have a single primary responsibility.

## Rule 2
Avoid oversized multi-purpose files.

## Rule 3
All modules should remain replaceable.

## Rule 4
Keep module communication simple and documented.

## Rule 5
Avoid hidden dependencies between systems.