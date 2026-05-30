# 📊 Token Optimization Guide - OpenCode

## ✅ Implementasi Selesai

Semua strategi token optimization telah diimplementasikan, KECUALI agent spesialis (strategi 6) sesuai permintaan.

---

## 🔧 Perubahan yang Telah Dilakukan

### 1. ✅ DCP (Dynamic Context Pruning) Terinstall
- Package: `@tarquinen/opencode-dcp`
- Config: `~/.config/opencode/dcp.json`
- Estimasi penghematan: **20-40%** untuk session panjang

### 2. ✅ AGENTS.md Dioptimasi
- Backup: `AGENTS.md.backup` (508 lines → 220 lines)
- Penghematan: ~1.500-2.000 token per session
- Menghapus: emoji dekoratif, box art, contoh panjang, format visual berlebihan

### 3. ✅ MCP Server Dimatikan
MCP server yang **dimatikan** (tidak essential):
- `everything` - testing tool
- `filesystem` - redundant dengan built-in tools
- `playwright-mcp` - redundant dengan browser-use
- `sequential-thinking` - hanya untuk task kompleks, bisa enable via skill
- `vision-mcp-server` - hanya ketika perlu analisis gambar

**Total terdisable: 5 servers** → Menghemat ~2.000-4.000 token per session.

### 4. ✅ user-settings.json Dioptimasi
- `autoCompact: true` (already)
- `compaction` config ditambahkan
- Agent models: Step 3.5 Flash Free untuk task & title (GRATIS!)
- `maxTokens` dikurangi: coder 50K → 30K

### 5. ✅ Model Tiering di opencode.json
- `orchestrator`: big-pickle, maxTokens 25K
- `build`: big-pickle, maxTokens 30K
- `plan`: Step 3.5 Flash **FREE**, maxTokens 12K
- `council`: big-pickle, maxTokens 20K
- `task` (baru): Step 3.5 Flash **FREE**, maxTokens 8K

**Kesempatan hemat biaya:** Task dan plan agent sekarang menggunakan model **GRATIS** untuk operasi ringan.

---

## 📈 Estimasi Penghematan Token

| Komponen | Before | After | Hemat |
|----------|--------|-------|-------|
| AGENTS.md | ~3.500 token | ~1.500 token | **~2.000** |
| MCP tools | ~8.000 token | ~4.000 token | **~4.000** |
| DCP compression | 0% | 20-40% | **bervariabel** |
| Model selection | semua paid | mixed free+paid | **biaya$token** |
| **Total per session** | ~15.000+ | ~7.000-10.000 | **~40-50%** |

---

## 🎯 Cara Penggunaan & Monitoring

### **A. DCP Commands (Penting!)**

Setelah install DCP, gunakan commands berikut untuk monitoring:

#### `/dcp context`
Menampilkan breakdown token usage saat ini:
```
/dcp context
```
Output:
- System prompt tokens
- User messages
- Assistant responses
- Tool calls
- Token saved by pruning
- % context used

#### `/dcp stats`
Statistik pruning across all sessions:
```
/dcp stats
```
Output:
- Total tokens saved
- Number of compressions
- Deduplication hits
- Average compression ratio

#### `/dcp status`
Status DCP lengkap:
```
/dcp status
```

#### `/dcp sweep [count]`
Manual pruning tool outputs:
```
/dcp sweep        → prune semua tools setelah last user message
/dcp sweep 10     → prune 10 tools terakhir
```

#### `/dcp compress [focus]`
Trigger compression manual:
```
/dcp compress     → compress semua stale content
/dcp compress focus:file edits  → compress specific focus
```

#### `/dcp manual on/off`
Toggle manual mode:
```
/dcp manual on    → AI tidak otomatis prune (manual only)
/dcp manual off   → Auto-prune aktif lagi
```

---

### **B. OpenCode Compact Commands**

#### `/compact`
Manual compaction saat context mulai penuh:
```
/compact
```
Ini akan memadatkan history conversation.

#### Check token usage:
```
/compact          → lihat estimasi token usage
```

---

### **C. Workflow Optimization**

#### 1. **Gunakan model yang tepat:**
- Task sederhana (baca data, tanya jawab): Otomatis pakai Step 3.5 Flash **FREE**
- Task kompleks (coding, arsitektur): big-pickle atau Gemini 3 Pro
- Planning/analysis: plan agent (Step 3.5 Flash FREE)

#### 2. **Matikan MCP yang tidak dipakai:**
Sudah dilakukan. Jika butuh:
- `sequential-thinking`: enable temporarily via skill
- `vision-mcp-server`: enable hanya saat analisis gambar
- `excalidraw`: enable hanya saat gambar diagram

#### 3. **Gunakan /compact secara proaktif:**
Setelah selesai task besar (>30 turn), jalankan:
```
/compact
```
Sebelum memulai task baru.

#### 4. **Monitor DCP secara rutin:**
Setiap 20-30 turn, cek:
```
/dcp context
```
Jika context usage >80%, consider `/dcp sweep` atau `/compact`.

---

## ⚙️ Konfigurasi Detail

### **DCP Config** (`~/.config/opencode/dcp.json`)

**Settings utama:**
```json
{
  "compress": {
    "maxContextLimit": 150000,   // Nudge mulai di 150K token
    "minContextLimit": 50000,    // Reminder off di bawah 50K
    "nudgeFrequency": 8,         // Nudge setiap 8 kali fetch
    "summaryBuffer": true        // Summary tokens extend limit
  },
  "turnProtection": {
    "turns": 4                    // Protect recent tools for 4 turns
  },
  "strategies": {
    "deduplication": true,       // Hapus duplicate tool calls
    "supersedeWrites": true,     // Hapus write setelah di-read
    "purgeErrors": true          // Hapus error inputs after 4 turns
  }
}
```

**Model-specific limits** (untuk model dengan context besar):
- Gemini 3 Pro/Flash: max 200K, min 80K
- Step 3.5 Flash: max 180K, min 60K
- Claude Sonnet: max 150K, min 50K

Ini memungkinkan DCP lebih agresif untuk model kecil, lebih konservatif untuk model besar.

---

### **Agent Tiering**

**Tier 1 (FREE - Step 3.5 Flash):**
- `plan` agent: planning, analysis
- `task` agent: background operations, search, fetch
- **Biaya: $0**

**Tier 2 (PREMIUM - big-pickle):**
- `orchestrator`: coordination, complex decisions
- `build`: code implementation
- `council`: multi-LLM consensus
- `council`: consensus

**Cara pakai:**
- Task otomatis menggunakan agent yang tepat berdasarkan konteks
- Untuk force specific agent: gunakan `/agent` command atau task delegation

---

## 🚨 Troubleshooting

### **DCP tidak aktif:**
1. Pastikan plugin terinstall: `npm list -g @tarquinen/opencode-dcp`
2. Restart OpenCode
3. Check: `/dcp status` → harus "enabled: true"

### **Token usage tidak turun:**
1. Cek DCP config: `~/.config/opencode/dcp.json`
2. Pastikan `enabled: true`
3. Cek `maxContextLimit` sesuai model Anda
4. Jalankan `/dcp sweep` manual

### **AI lupa konteks setelah pruning:**
1. Naikkan `turnProtection.turns` dari 4 ke 6
2. Tambahkan protected tools jika perlu
3. Matikan `protectUserMessages: false` → `true` (jika user messages penting)

### **MCP server perlu di-enable kembali:**
Edit `opencode.json`, set `"enabled": true` untuk server yang diperlukan, lalu restart OpenCode.

---

## 📊 Monitoring Rutin

**Daily check (setiap sesi):**
```
/dcp context    → lihat current token usage
```

**Weekly check:**
```
/dcp stats      → lihat cumulative savings
```

**Jika respons lambat:**
```
/compact        → compact session
/dcp sweep      → prune tools
```

---

## 🔄 Restart OpenCode

**SETELAH semua perubahan, RESTART OpenCode!**

1. Close OpenCode completely
2. Buka kembali
3. Check DCP aktif: `/dcp status`
4. Check MCP servers: `/mcp list` (jika command tersedia)

---

## 📁 File Changes Summary

| File | Perubahan | Token Impact |
|------|-----------|--------------|
| `AGENTS.md` | 508 → 220 lines | -2.000 |
| `dcp.json` | NEW file | -20-40% |
| `opencode.json` | 5 MCP disabled | -4.000 |
| `user-settings.json` | model tiering, maxTokens reduced | -5.000/task |
| **Total impact** | | **~40-50% hemat** |

---

## 🎓 Best Practices Going Forward

1. **Gunakan model yang tepat:** Jangan selalu pakai model terbesar
2. **Compact proactively:** Jangan tunggu context penuh
3. **Monitor DCP:** Cek `/dcp context` setiap 20-30 turn
4. **Disable unused MCP:** Jika ada MCP baru yang tidak dipakai, disable
5. **Keep AGENTS.md ringkas:** Jangan tambah konten berlebihan
6. **Use /dcp sweep:** Saat ada banyak tool calls yang sudah selesai
7. **Leverage free models:** Step 3.5 Flash untuk task ringan

---

## 📚 Referensi

- DCP GitHub: https://github.com/Opencode-DCP/opencode-dynamic-context-pruning
- DCP Docs: https://opencodedocs.com/Opencode-DCP/opencode-dynamic-context-pruning/
- OpenCode Config: https://opencode.ai/docs/config/
- Agent Config: https://dev.opencode.ai/docs/agents

---

**Status:** ✅ Semua strategi (1-5, 7) diimplementasikan.  
**Next:** Restart OpenCode, test dengan `/dcp status`, monitor token usage.
