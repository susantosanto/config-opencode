---
name: superpowers-systematic-debugging
description: "Use when: Ada bug/test failure/unexpected behavior - Systematic 4-phase debugging SEBELUM fix"
---

# Systematic Debugging - Superpowers

**Core Principle: ALWAYS find root cause BEFORE attempting fixes. Symptom fixes are failure.**

## The Iron Law
```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## Four Phases

### Phase 1: Root Cause Investigation
1. **Read Error Messages Carefully** - Don't skip errors/warnings
2. **Reproduce Consistently** - Can you trigger it reliably?
3. **Check Recent Changes** - What changed that could cause this?
4. **Gather Evidence** - For multi-component systems, add diagnostic instrumentation
5. **Trace Data Flow** - Trace bad value back to origin

### Phase 2: Pattern Analysis
1. **Find Working Examples** - Locate similar working code
2. **Compare Against References** - Read reference implementations COMPLETELY
3. **Identify Differences** - What's different between working and broken?
4. **Understand Dependencies** - What settings, config, environment needed?

### Phase 3: Hypothesis and Testing
1. **Form Single Hypothesis** - "I think X is root cause because Y"
2. **Test Minimally** - Smallest possible change to test
3. **Verify Before Continuing** - Work? → Phase 4. No? → New hypothesis

### Phase 4: Implementation
1. **Create Failing Test Case** - MUST have before fixing
2. **Implement Single Fix** - Address root cause, ONE change at a time
3. **Verify Fix** - Test passes? No other tests broken?
4. **If 3+ Fixes Failed** → Question architecture!

## Red Flags - STOP!
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- Proposing solutions before tracing data flow
- "One more fix attempt" (when already tried 2+)

## Kapan Digunakan
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

## Contoh Penggunaan
```
use skill tool to load superpowers/systematic-debugging
```