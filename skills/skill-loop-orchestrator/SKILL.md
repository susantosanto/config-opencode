---
name: skill-loop-orchestrator
description: "Orchestrate multi-skill loop workflows for AI agents. Chain skills, set routing rules, and run iterative implement-review-rework cycles. Use when user says 'run loop', 'loop workflow', 'orchestrate skills', 'chain skills', 'skill pipeline', or 'build loop'."
---

# Skill Loop Orchestrator

Chain multiple skills into iterative loop-based workflows. Each skill runs, a router evaluates output, and the workflow advances or reworks based on criteria.

## When to Use

- User wants to chain multiple skills in sequence
- User wants iterative implement → review → rework cycles
- User wants automated task execution with quality gates
- User says "loop this", "run in a loop", "chain skills"

## Workflow Pattern

```
┌─────────┐     ┌──────────┐     ┌────────┐
│  skill  │ ──▶ │  router  │ ──▶ │ decide │
│  exec   │     │ evaluate │     │        │
└─────────┘     └──────────┘     └────────┘
     ▲               │               │
     │               ▼               │
     │          done/approve ◀───────┤
     │               │               │
     └──── rework ◀──┘           blocked
```

## How to Orchestrate

### Step 1: Define the Loop Config

Create a loop config (either inline or in a file):

```yaml
name: feature-implementation
max_iterations: 5
default_entrypoint: implement

skills:
  implement:
    description: "Write the code for the feature"
    next:
      - id: to-review
        skill: review

  review:
    description: "Review code quality, test coverage, architecture"
    next:
      - id: approve
        criteria: "All tests pass, code follows best practices, no critical issues"
        done: true
      - id: rework
        criteria: "Tests fail or code quality issues found"
        skill: implement
      - id: escalate
        criteria: "Design decision needed from human"
        blocked: true
```

### Step 2: Execute the Loop

For each iteration:

1. **Run the current skill** with the task context
2. **Capture stdout/output** from the skill
3. **Route the output** through the router evaluation
4. **Decide next step**: done, rework, or blocked

### Step 3: Router Evaluation

The router evaluates skill output against criteria:
- Parse skill output for success/failure signals
- Check if criteria are met
- Return routing decision with reason

## Built-in Loop Patterns

### Pattern A: Implement → Review → Rework

Best for: Feature development, bug fixes

```
implement → review → {approve | rework → implement}
```

### Pattern B: Plan → Execute → Verify

Best for: Multi-step tasks, migrations

```
plan → execute → verify → {next-task | fix → execute}
```

### Pattern C: Write → Test → Fix

Best for: TDD, test-driven development

```
write-code → run-tests → {pass | fix → run-tests}
```

### Pattern D: Multi-Agent Review

Best for: Architecture decisions, critical code

```
agent-a-implements → agent-b-reviews → agent-c-tests → {approve | rework}
```

## Termination Conditions

Always define clear exit conditions:

| Condition | Description |
|-----------|-------------|
| `done: true` | Criteria met, loop ends successfully |
| `blocked: true` | Human input needed, loop pauses |
| `max_iterations` | Safety limit reached |
| `error_threshold` | Too many consecutive failures |

## Integration with Other Skills

This orchestrator works with:
- `implement-review-loop` — for code implementation cycles
- `self-improvement-loop` — for skill quality improvement
- `design-architecture-loop` — for architecture design cycles
- Any custom skill that produces stdout output

## Example: Full Feature Loop

```yaml
name: full-feature
max_iterations: 10
skills:
  plan:
    description: "Break down feature into tasks"
    next:
      - skill: implement

  implement:
    description: "Write code for current task"
    next:
      - skill: test

  test:
    description: "Run all tests"
    next:
      - id: pass
        criteria: "All tests pass"
        skill: review
      - id: fail
        criteria: "Tests fail"
        skill: implement

  review:
    description: "Code review against best practices"
    next:
      - id: approve
        criteria: "No critical issues, follows conventions"
        done: true
      - id: rework
        criteria: "Issues found"
        skill: implement
```
