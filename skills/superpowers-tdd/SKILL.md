---
name: superpowers-tdd
description: "Use when: Mau implement fitur/bugfix - Test-Driven Development SEBELUM production code"
---

# Test-Driven Development - Superpowers

**Core Principle: Write test FIRST, watch it fail, write minimal code, watch it pass**

## The Iron Law
```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

## Red-Green-Refactor Cycle

### RED - Write Failing Test
- Write one minimal test showing what should happen
- Clear name, tests real behavior, one thing

### VERIFY RED - Watch It Fail (MANDATORY)
```bash
npm test path/to/test.test.ts
```
Confirm test fails for expected reason (feature missing, not typo)

### GREEN - Minimal Code
- Write simplest code to pass the test
- DON'T add features, refactor, or "improve" beyond the test

### VERIFY GREEN - Watch It Pass (MANDATORY)
```bash
npm test path/to/test.test.ts
```
Confirm test passes, other tests still pass, output pristine

### REFACTOR - Clean Up
- Remove duplication
- Improve names
- Extract helpers
- Keep tests green

## Kapan Digunakan
- New features
- Bug fixes
- Refactoring
- Behavior changes

## Exceptions (ask user):
- Throwaway prototypes
- Generated code
- Configuration files

## Common Rationalizations to Avoid
- "Too simple to test" → Simple code breaks
- "I'll test after" → Tests passing immediately prove nothing
- "Already manually tested" → Ad-hoc ≠ systematic
- "TDD will slow me down" → TDD faster than debugging

## Contoh Penggunaan
```
use skill tool to load superpowers/test-driven-development
```