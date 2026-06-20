---
name: self-improvement-loop
description: "Recursive self-improvement loop for AI agent skills. Studies a skill, forms improvement hypothesis, builds variant, tests against champion, promotes winner. Use when user says 'improve this skill', 'optimize skill', 'self-improve', 'make skill better', 'skill RSI', or 'recursive skill improvement'."
---

# Self-Improvement Loop

Recursive loop that studies, tests, and improves AI agent skills through controlled experiments.

## When to Use

- User wants to improve an existing skill
- User wants to optimize skill prompts/instructions
- User says "make this skill better", "improve quality"
- User wants data-driven skill evolution

## Loop Flow

```
┌─────────────────────────────────────────────┐
│           1. STUDY DOMAIN                   │
│  • Research the skill's purpose            │
│  • Identify success criteria               │
│  • Find failure modes                      │
│  • Compile ontology (excellence markers)   │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           2. DECONSTRUCT CHAMPION           │
│  • Break skill into testable surfaces      │
│  • Each surface: hypothesis + metric       │
│  • Identify regression risks               │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           3. GENERATE CHALLENGER            │
│  • Change ONE variable at a time           │
│  • Localized modification                  │
│  • Preserve what works                     │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           4. EVALUATE                       │
│  • Run champion vs challenger              │
│  • Same prompts, same criteria             │
│  • Measure output quality                  │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│           5. PROMOTE OR KEEP               │
│  • If challenger wins → new champion       │
│  • If champion wins → keep                 │
│  • Record results + dead ends              │
└──────────────────┬──────────────────────────┘
                   ↓
            [LOOP TO STEP 2]
```

## Step 1: Study the Domain

Before modifying anything, build an ontology:

```markdown
## Skill Ontology: [skill-name]

### Purpose
- What problem does this skill solve?
- Who is the user?
- What does excellent output look like?

### Excellence Markers
- [specific quality indicator 1]
- [specific quality indicator 2]
- [specific quality indicator 3]

### Failure Modes
- [common failure 1]
- [common failure 2]
- [common failure 3]

### Authorities
- [expert/practice that defines "good" for this domain]
```

## Step 2: Deconstruct the Champion

Break the skill into testable components:

```markdown
## Deconstruction: [skill-name]

### Surface 1: Prompt Clarity
- Hypothesis: "Clearer instructions improve output consistency"
- Metric: Output matches requirements on first attempt
- Regression risk: Low

### Surface 2: Edge Case Handling
- Hypothesis: "Explicit edge case instructions reduce failures"
- Metric: Success rate on unusual inputs
- Regression risk: Medium

### Surface 3: Output Format
- Hypothesis: "Structured output format improves usability"
- Metric: Output can be directly consumed without reformatting
- Regression risk: Low
```

## Step 3: Generate Challenger

Rules for challenger generation:
1. **One variable change** — only modify one aspect
2. **Minimal edit** — smallest change that tests the hypothesis
3. **Preserve structure** — don't rewrite from scratch
4. **Document the change** — explain what changed and why

## Step 4: Evaluate

Run controlled comparison:

```markdown
## Evaluation Report

### Test Prompts
1. [prompt 1]
2. [prompt 2]
3. [prompt 3]

### Champion Output
- Prompt 1: [quality score]
- Prompt 2: [quality score]
- Prompt 3: [quality score]
- Average: [score]

### Challenger Output
- Prompt 1: [quality score]
- Prompt 2: [quality score]
- Prompt 3: [quality score]
- Average: [score]

### Verdict
- Winner: [champion/challenger]
- Improvement: [+X%]
- Confidence: [high/medium/low]
```

## Step 5: Record and Iterate

Keep a history of all experiments:

```markdown
## Experiment Log

### Exp 1: Added explicit output format
- Change: Added JSON schema example
- Result: Champion won (+2%)
- Lesson: Format was already clear enough

### Exp 2: Added edge case handling
- Change: Added "handle empty input" instruction
- Result: Challenger won (+15%)
- Promotion: New champion

### Exp 3: Shortened prompt length
- Change: Removed 30% of instructions
- Result: Champion won (-8%)
- Lesson: Instructions were necessary, not redundant
```

## Termination Conditions

| Condition | Action |
|-----------|--------|
| 10 iterations completed | Stop, report best champion |
| 3 consecutive no-improvements | Stop, diminishing returns |
| Challenger consistently wins | Continue until plateau |
| Manual stop requested | Save current state, report |

## Integration

- Use with `skill-loop-orchestrator` for automated improvement pipelines
- Output improved skills to `.opencode/skills/` or `.claude/skills/`
- Combine with `design-architecture-loop` for architecture-focused skills
