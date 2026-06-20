---
name: implement-review-loop
description: "Iterative implement → review → rework loop for code quality. Writes code, runs tests/linter/typecheck, reviews against best practices, and fixes until quality gate passes. Use when user says 'implement and review', 'code loop', 'write and check', 'implement until passing', or 'quality loop'."
---

# Implement-Review Loop

Automated loop that implements code, validates quality, and reworks until all gates pass.

## When to Use

- User wants code written with automatic quality validation
- User wants implement → test → review → fix cycles
- User says "implement this and make sure it passes all checks"
- User wants zero-human-intervention code quality

## Loop Flow

```
┌─────────────────────────────────────────────┐
│              IMPLEMENT PHASE                 │
│  • Read requirements/context                │
│  • Write or modify code                     │
│  • Follow project conventions               │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│              VALIDATE PHASE                  │
│  • Run typecheck (tsc --noEmit)             │
│  • Run linter (eslint)                      │
│  • Run unit tests                           │
│  • Run build                                │
└──────────────────┬──────────────────────────┘
                   ↓
            ┌──────────────┐
            │  ALL PASS?   │
            └──────┬───────┘
              yes  │  no
               ↓   ↓
┌──────────┐  ┌──────────────────┐
│  REVIEW  │  │  ANALYZE ERROR   │
│  PHASE   │  │  • Read error    │
└────┬─────┘  │  • Find cause    │
     │        │  • Plan fix      │
     ↓        └────────┬────────┘
┌──────────┐           │
│ APPROVE? │           ↓
└────┬─────┘  ┌──────────────────┐
  yes│  no    │  FIX & RETRY     │
     ↓        │  • Apply fix     │
  ┌──────┐    │  • Re-validate   │
  │ DONE │    └──────────────────┘
  └──────┘
```

## Quality Gates (in order)

### Gate 1: Type Safety
```bash
# TypeScript
npx tsc --noEmit

# Python
mypy . || python -m py_compile *.py
```

### Gate 2: Linting
```bash
# JavaScript/TypeScript
npx eslint . --max-warnings 0

# Python
ruff check . || flake8 .
```

### Gate 3: Unit Tests
```bash
# Jest/Vitest
npx vitest run || npx jest

# Python
pytest -x --tb=short
```

### Gate 4: Build
```bash
# Node.js
npm run build || pnpm build

# Go
go build ./...

# Rust
cargo build
```

## Error Analysis Template

When a gate fails, analyze:

```
ERROR ANALYSIS:
- Gate: [typecheck/lint/test/build]
- Error: [exact error message]
- File: [file path]
- Line: [line number]
- Root cause: [what went wrong]
- Fix plan: [how to fix]
- Risk: [what might break]
```

## Rework Rules

1. **One fix per iteration** — don't try to fix everything at once
2. **Preserve passing gates** — don't break what already works
3. **Minimal changes** — smallest possible fix
4. **Verify the fix** — re-run the failed gate before moving on

## Termination

| Condition | Action |
|-----------|--------|
| All 4 gates pass | Loop ends, report success |
| 5 consecutive failures on same gate | Escalate to human |
| Fix introduces new failures | Revert and try different approach |

## Context to Pass Between Iterations

```yaml
iteration_context:
  task: "original task description"
  attempt: 3
  previous_errors:
    - gate: typecheck
      error: "Property 'name' does not exist on type 'User'"
      file: "src/user.ts"
      line: 42
  fixes_applied:
    - "Added 'name' field to User interface"
  files_modified:
    - "src/user.ts"
    - "src/types.ts"
```

## Integration

- Use with `skill-loop-orchestrator` for multi-task loops
- Use with `design-architecture-loop` when architectural review is needed
- Works with any project that has typecheck/lint/test/build commands
