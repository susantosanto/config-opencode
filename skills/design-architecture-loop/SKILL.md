---
name: design-architecture-loop
description: "Iterative design-architecture loop for software systems. Plans architecture, implements skeleton, reviews against design principles, and reworks until architecture is sound. Use when user says 'design loop', 'architecture review', 'plan and implement', 'design first', or 'architect this'."
---

# Design-Architecture Loop

Iterative loop that plans, implements skeleton, and reviews against software design principles.

## When to Use

- User wants to design before coding
- User wants architecture review against SOLID/Clean Architecture
- User says "design this feature first", "architect this system"
- User wants to ensure code quality from the start

## Loop Flow

```
┌─────────────────────────────────────────────┐
│           1. DESIGN PHASE                   │
│  • Understand requirements                 │
│  • Identify components & boundaries        │
│  • Choose patterns (if applicable)         │
│  • Create design document                  │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           2. SKELETON PHASE                 │
│  • Create directory structure              │
│  • Define interfaces/types                 │
│  • Create stub implementations            │
│  • Set up tests skeleton                   │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           3. REVIEW PHASE                   │
│  • API Design Review                       │
│  • OO Design Review (SOLID)                │
│  • Clean Architecture Review               │
│  • Dependency Analysis                     │
└──────────────────┬──────────────────────────┘
                   ↓
            ┌──────────────┐
            │  ALL PASS?   │
            └──────┬───────┘
              yes  │  no
               ↓   ↓
┌──────────┐  ┌──────────────────┐
│ APPROVE  │  │  REDESIGN        │
│ & PROCEED│  │  • Fix issues    │
└──────────┘  │  • Update design │
              └──────────────────┘
```

## Design Phase Checklist

### Requirements Analysis
- [ ] What problem does this solve?
- [ ] Who are the users/actors?
- [ ] What are the inputs/outputs?
- [ ] What are the constraints?
- [ ] What are the non-functional requirements?

### Component Design
- [ ] Identify major components
- [ ] Define component boundaries
- [ ] Specify interfaces between components
- [ ] Choose data flow patterns
- [ ] Identify shared state

### Pattern Selection
- [ ] Creational patterns (Factory, Builder, Singleton)
- [ ] Structural patterns (Adapter, Facade, Proxy)
- [ ] Behavioral patterns (Strategy, Observer, Command)
- [ ] Architecture patterns (MVC, MVVM, Hexagonal, Event-Driven)

## Review Phase: Three Reviewers

### 1. API Design Review

Check:
- Naming conventions (consistent, descriptive)
- Method signatures (clear parameters, return types)
- Parameter design (required vs optional, defaults)
- Type safety (no `any`, proper generics)
- REST conventions (if applicable): resource nouns, HTTP verbs, status codes

### 2. OO Design Review (SOLID)

Check:
- **S**ingle Responsibility: Each class has one reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes are substitutable
- **I**nterface Segregation: Many specific interfaces over general
- **D**ependency Inversion: Depend on abstractions, not concretions
- **DRY**: No duplicated logic
- **Composition over Inheritance**: Prefer composition

### 3. Clean Architecture Review

Check:
- **Component Cohesion**: REP, CRP, CCP
- **Component Coupling**: ADP, SDP, SAP
- **Dependency Rule**: Dependencies point inward (entities → use-cases → adapters → frameworks)
- **Boundary Crossing**: Use dependency inversion at boundaries
- **Testability**: Core logic is independently testable

## Design Document Template

```markdown
# Design: [Feature/System Name]

## Overview
[What and why]

## Components
### [Component 1]
- Responsibility: [...]
- Interface: [...]
- Dependencies: [...]

### [Component 2]
- Responsibility: [...]
- Interface: [...]
- Dependencies: [...]

## Data Flow
[How data moves through the system]

## Patterns Used
- [Pattern 1]: [Why chosen]

## Trade-offs
- [Accepted trade-off 1]
- [Accepted trade-off 2]

## Risks
- [Risk 1]: [Mitigation]

## Files to Create/Modify
- `src/path/file.ts` — [purpose]
```

## Termination

| Condition | Action |
|-----------|--------|
| All 3 reviewers pass | Design approved, proceed to implementation |
| Critical issues found | Redesign required |
| 3 iterations without improvement | Escalate to human architect |

## Integration

- Use before `implement-review-loop` for design-first development
- Use with `skill-loop-orchestrator` for automated design pipelines
- Feed design document into implementation skills
