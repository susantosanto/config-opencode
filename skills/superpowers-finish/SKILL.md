---
name: superpowers-finish
description: "Use when: Semua task sudah complete - Verifikasi, cleanup, dan merge/PR decision"
---

# Finishing a Development Branch - Superpowers

**Use when: Semua tasks sudah complete, mau finish branch**

## Proses
1. **Verify all tests pass**
2. **Present options ke user:**
   - Merge to main (if authorized)
   - Create PR for review
   - Keep branch for later
   - Discard branch
3. **Execute user's choice**
4. **Cleanup worktree** (jika menggunakan git worktrees)

## Verification Checklist
- [ ] All tests pass
- [ ] No lint errors
- [ ] Code coverage maintained/increased
- [ ] Documentation updated
- [ ] No debug/console logs left

## Contoh Penggunaan
```
use skill tool to load superpowers/finishing-a-development-branch
```

## Integration with Workflow
- After subagent-driven-development completes all tasks
- Before merging ke main/master branch