---
name: superpowers-code-review
description: "Use when: Mau review code sebelum merge - Pre-merge code review checklist"
---

# Requesting Code Review - Superpowers

**Core Principle: Review early, review often**

## Kapan Request Review
- **Mandatory:** After each task in subagent-driven development, after completing major feature, before merge to main
- **Optional:** When stuck, before refactoring, after fixing complex bug

## How to Request
1. Get git SHAs:
```bash
BASE_SHA=$(git rev-parse HEAD~1)
HEAD_SHA=$(git rev-parse HEAD)
```

2. Dispatch code-reviewer subagent dengan template

3. Act on feedback:
- Fix **Critical** issues immediately
- Fix **Important** issues before proceeding
- Note **Minor** issues for later
- Push back if reviewer wrong (with reasoning)

## Issue Severity
- **Critical** - Block merge, must fix
- **Important** - Should fix before proceeding
- **Minor** - Note for later

## Contoh Penggunaan
```
use skill tool to load superpowers/requesting-code-review
```

## Integration
- **Subagent-Driven Development**: Review after EACH task
- **Executing Plans**: Review after each batch (3 tasks)
- **Ad-Hoc**: Review before merge