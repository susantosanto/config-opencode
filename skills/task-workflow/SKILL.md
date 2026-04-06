---
name: task-workflow
description: Automatically structures every task into a 6-phase workflow: Goal, Instructions, Discoveries, Accomplished, Relevant files/directories, Next Steps. Use this skill whenever the user asks for ANY task or request - this ensures systematic task completion with clear tracking and progress visibility. This skill should ALWAYS trigger on any user request, no matter how small, to provide consistent structured task management.
---

# Task Workflow Skill

This skill ensures every task is approached systematically with clear progress tracking. Every user request triggers this workflow automatically.

## When to Trigger

- **ALWAYS trigger** when the user makes ANY request, statement, or gives a task
- This includes simple requests like "help me", "do this", questions, or any action
- Do NOT ask the user to enable this - it should be automatic for every interaction

## Workflow Structure

Every task MUST follow this 6-phase structure:

### Phase 1: GOAL
- **What**: Clearly state what the user wants to accomplish
- **Format**: Single clear statement of the objective
- **Why**: Establishes clear direction before proceeding

### Phase 2: INSTRUCTIONS
- **What**: How to accomplish the task - specific steps to take
- **Format**: Numbered list of actionable steps
- **Why**: Provides a clear execution plan

### Phase 3: DISCOVERIES
- **What**: What you find/learn during the task execution
- **Format**: List of findings, observations, and relevant information
- **Why**: Documents knowledge gained and informs decisions

### Phase 4: ACCOMPLISHED
- **What**: What has been completed successfully
- **Format**: List of completed items and results achieved
- **Why**: Shows progress and deliverables

### Phase 5: RELEVANT FILES/DIRECTORIES
- **What**: Files and directories involved in the task
- **Format**: List with brief descriptions of relevance
- **Why**: Provides context and reference points

### Phase 6: NEXT STEPS
- **What**: What comes after this task
- **Format**: List of follow-up actions or recommendations
- **Why**: Ensures continuity and completeness

## Execution Rules

1. **NEVER skip any phase** - all 6 must be present
2. **Use this exact format** for every response
3. **Complete phases in order** - Goal → Instructions → Discoveries → Accomplished → Relevant Files → Next Steps
4. **Keep each phase concise** but informative
5. **After completing the task**, present the full workflow summary

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 GOAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Clear statement of what user wants]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 INSTRUCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Step 1]
2. [Step 2]
3. [Step 3]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 DISCOVERIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Finding 1]
- [Finding 2]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ACCOMPLISHED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Completed item 1]
- [Completed item 2]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 RELEVANT FILES/DIRECTORIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [File/Dir 1]: [Description]
- [File/Dir 2]: [Description]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👉 NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Next step 1]
- [Next step 2]
...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Important Notes

- If there are no discoveries, write "None" - do not skip
- If there are no relevant files, write "None" - do not skip
- If there are no next steps, write "None" - do not skip
- Update the phases as you work through the task
- Show the complete workflow in your final response