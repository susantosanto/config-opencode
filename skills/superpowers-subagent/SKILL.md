---
name: superpowers-subagent
description: "Use when: Mau execute implementation plan dengan parallel subagents dalam current session"
---

# Subagent-Driven Development - Superpowers

**Execute plan by dispatching fresh subagent per task + two-stage review**

## Why Subagents
- Fresh subagent per task (no context pollution)
- Two-stage review: spec compliance first, then code quality
- High quality + fast iteration

## The Process
1. Read plan, extract all tasks
2. Per task:
   - Dispatch implementer subagent
   - Implementer asks questions? → Answer
   - Implementer implements, tests, commits, self-reviews
   - Dispatch spec reviewer subagent → Confirm matches spec?
   - If issues: Implementer fixes → re-review
   - Dispatch code quality reviewer → Approves?
   - If issues: Implementer fixes → re-review
   - Mark task complete
3. After all tasks: Final code review
4. Finish branch

## Model Selection
- Mechanical (1-2 files, clear spec) → Fast/cheap model
- Integration (multi-file) → Standard model
- Architecture/design → Most capable model

## Required Skills
- **using-git-worktrees** - Set up isolated workspace SEBELUM mulai
- **writing-plans** - Creates the plan
- **requesting-code-review** - Code review template
- **finishing-a-development-branch** - Complete development

## Contoh Penggunaan
```
use skill tool to load superpowers/subagent-driven-development
```