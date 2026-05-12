# Graphify Workflow Guide untuk OpenCode

## 📋 Quick Reference

```
/graphify <path>              # Build graph untuk folder
/graphify <path> --update    # Incremental update
/graphify <path> --mode deep # Thorough extraction
```

---

## 🎯 Common Use Cases

### 1. Understanding Codebase Baru
```
# Trigger: "Apa struktur project ini?" atau "File mana yang penting?"
/graphify .
```
→ Baca `graphify-out/GRAPH_REPORT.md` untuk god nodes + communities

### 2. Mencari Fungsi/Class
```
# Tanya: "Where is X function?"
graphify query "X function"    # BFS traversal
graphify query "X" --dfs    # DFS untuk trace spesifik
```

### 3. Trace Relationship
```
# Tanya: "How does A relate to B?"
graphify path "A" "B"
```

### 4. Penjelasan Node
```
# Tanya: "What is X?"
graphify explain "X"
```

---

## 🔄 Update Workflows

### Scenario: Mengedit Code
```
# Setelah edit, update graph:
graphify update .

# Atau rebuild cluster:
graphify cluster-only .
```

### Scenario: Menambah File Baru
```
graphify update .
```

---

## 📊 Output Files

| File | Fungsi |
|------|--------|
| `graph.html` | Interactive visualization (buka di browser) |
| `graph.json` | Queryable knowledge graph |
| `GRAPH_REPORT.md` | Audit report dengan god nodes |

---

## ⚡ Quick Commands

```bash
# Full pipeline
graphify .

# Skip visualization (hanya JSON + report)
graphify . --no-viz

# Thorough (richer edges, lebih detail)
graphify . --mode deep

# Query existing graph
graphify query "apa fungsi X"

# Shortest path antara dua konsep
graphify path "AuthModule" "Database"
```

---

## 📝 Contoh Percakapan

**User**: "Apa arsitektur project ini?"
→ **Anda**: `/graphify .` → baca GRAPH_REPORT.md → jelaskan

**User**: "Dimana fungsi login?"
→ **Anda**: `graphify query "login"` → kasih lokasi

**User**: "Bagaimana hubungan antar agent?"
→ **Anda**: `graphify path "Orchestrator" "Council"` → jelaskan

---

## 🔧 Maintenance

```bash
# Check jika perlu update
graphify check-update .

# Watch mode (auto-rebuild on change)
graphify watch .
```

---

Generated: 2026-04-28
Graphify v0.5.4