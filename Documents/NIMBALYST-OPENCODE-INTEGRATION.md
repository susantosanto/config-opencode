# 🔧 Panduan Integrasi OpenCode dengan Nimbalyst

## 📋 Diagnosa Masalah

**Error:** `OpenCode server failed to start within 30000ms`

**Root Cause:** Nimbalyst (aplikasi Electron) mencoba menjalankan command `opencode acp` sebagai subprocess, tetapi **tidak bisa menemukan binary `opencode` dalam PATH** yang tersedia untuk aplikasi Electron.

---

## 🔍 Analisis Situasi

### ✅ Yang Sudah Benar:
| Komponen | Status | Lokasi |
|----------|--------|--------|
| OpenCode CLI | ✅ Terinstall | `C:\Users\USER\AppData\Roaming\npm\opencode.cmd` |
| Binary Asli | ✅ Ada | `C:\Users\USER\AppData\Roaming\npm\node_modules\opencode-ai\bin\opencode.exe` |
| Auth Providers | ✅ Terkonfigurasi | `C:\Users\USER\.local\share\opencode\auth.json` |
| Providers Aktif | ✅ 12 providers | opencode, openrouter, google, kilo, nvidia, cerebras, mistral, cloudflare, zhipuai, dll |
| OpenCode Config | ✅ Ada | `C:\Users\USER\.config\opencode\opencode.json` |

### ❌ Masalah:
Nimbalyst adalah aplikasi **Electron** yang tidak selalu mewarisi PATH environment dari terminal Windows. Saat Nimbalyst mencoba spawn `opencode acp`, command tersebut tidak ditemukan.

---

## 🛠️ Solusi (Coba Berurutan)

### Solusi 1: Tambahkan OpenCode ke System PATH (REKOMENDASI)

Ini adalah solusi paling permanen dan akan memperbaiki masalah untuk semua aplikasi.

**Langkah-langkah:**

1. **Buka Environment Variables:**
   - Tekan `Win + R`
   - Ketik: `sysdm.cpl`
   - Klik tab **Advanced** → **Environment Variables**

2. **Edit PATH:**
   - Di bagian **User variables**, cari variabel `Path`
   - Klik **Edit** → **New**
   - Tambahkan: `C:\Users\USER\AppData\Roaming\npm`
   - Klik **OK** di semua dialog

3. **Verifikasi:**
   - Tutup dan buka ulang Nimbalyst
   - Coba enable OpenCode lagi di Settings → Agent Providers → OpenCode

**Atau via PowerShell (Run as Administrator):**
```powershell
# Tambahkan ke User PATH
$oldPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newPath = "$oldPath;C:\Users\USER\AppData\Roaming\npm"
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")

# Verifikasi
[Environment]::GetEnvironmentVariable("Path", "User") -split ";" | Select-String "npm"
```

---

### Solusi 2: Buat Wrapper Script (Jika Solusi 1 Tidak Bekerja)

Buat file batch yang memanggil OpenCode dengan path absolut:

**Langkah-langkah:**

1. **Buat folder untuk wrapper:**
```powershell
mkdir C:\Users\USER\bin
```

2. **Buat file `opencode.bat` di `C:\Users\USER\bin\`:**
```batch
@echo off
"C:\Users\USER\AppData\Roaming\npm\node_modules\opencode-ai\bin\opencode.exe" %*
```

3. **Tambahkan `C:\Users\USER\bin` ke PATH** (lihat Solusi 1)

---

### Solusi 3: Jalankan OpenCode Server Secara Manual

Jika Nimbalyst masih tidak bisa start OpenCode, jalankan server secara manual terlebih dahulu:

**Opsi A - ACP Mode (yang dibutuhkan Nimbalyst):**
```powershell
# Buka terminal baru
cd C:\Users\USER\.config\opencode
opencode acp
```

**Opsi B - HTTP Server Mode:**
```powershell
# Buka terminal baru
cd C:\Users\USER\.config\opencode
opencode serve --port 4096
```

Kemudian di Nimbalyst, coba connect ke server yang sudah running.

---

### Solusi 4: Set Environment Variable di Nimbalyst

Beberapa aplikasi Electron memungkinkan custom environment variables:

1. **Buka Settings Nimbalyst** → **Advanced**
2. **Cari bagian Environment/Tools**
3. **Tambahkan PATH** yang mencakup npm global:
   ```
   PATH=C:\Users\USER\AppData\Roaming\npm;%PATH%
   ```

---

### Solusi 5: Install OpenCode via Binary (Alternatif)

Jika install via npm bermasalah, install via binary langsung:

```powershell
# Download binary terbaru dari GitHub
# Kunjungi: https://github.com/anomalyco/opencode/releases

# Atau via Scoop (jika terinstall):
scoop install opencode

# Atau via Chocolatey (jika terinstall):
choco install opencode
```

---

## 🧪 Verifikasi Setelah Fix

### Test 1: Cek PATH
```powershell
# Buka terminal BARU (penting!)
where opencode
# Harus menampilkan: C:\Users\USER\AppData\Roaming\npm\opencode.cmd
```

### Test 2: Cek OpenCode Berjalan
```powershell
opencode --version
# Harus menampilkan versi OpenCode
```

### Test 3: Test ACP Mode
```powershell
# Test ACP mode (akan hang, tekan Ctrl+C untuk stop)
opencode acp
# Jika tidak error "command not found" = BERHASIL
```

### Test 4: Test di Nimbalyst
1. Buka Nimbalyst
2. **Settings** → **Agent Providers**
3. Toggle **Enable OpenCode**
4. Seharusnya tidak ada error timeout lagi

---

## 📖 Cara Kerja Integrasi OpenCode ↔ Nimbalyst

```
┌─────────────────────────────────────────────────────────┐
│                    NIMBALYST (Electron)                  │
│                                                          │
│  ┌─────────────┐    spawn("opencode acp")   ┌─────────┐ │
│  │  UI/Editor  │ ──────────────────────────▶│ OpenCode│ │
│  │             │ ◀──────────────────────────│  ACP    │ │
│  │  Session    │    JSON-RPC via stdio      │ Server  │ │
│  │  Management │                             └─────────┘ │
│  └─────────────┘                                    │   │
│                                                      ▼   │
│                                            ┌────────────┐│
│                                            │ LLM Provider││
│                                            │ (Kilo/Google)││
│                                            └────────────┘│
└─────────────────────────────────────────────────────────┘
```

**Protokol Komunikasi:**
- Nimbalyst spawn `opencode acp` sebagai subprocess
- Komunikasi via **JSON-RPC over stdio** (stdin/stdout)
- Nimbalyst mengirim request → OpenCode memproses → OpenCode mengirim response
- Timeout 30 detik jika OpenCode tidak start dalam waktu tersebut

---

## ⚠️ Troubleshooting Lanjutan

### Masalah: "Command not found" di Nimbalyst
**Penyebab:** PATH tidak terwaris ke aplikasi Electron
**Solusi:** Gunakan Solusi 1 atau 2 di atas

### Masalah: OpenCode start tapi langsung crash
**Penyebab:** Provider/API key tidak terkonfigurasi
**Solusi:**
```powershell
# Cek auth
opencode auth list

# Login jika perlu
opencode auth login
```

### Masalah: Timeout masih terjadi
**Penyebab:** MCP servers lambat start (terutama yang pakai uvx/python)
**Solusi:**
1. Disable MCP yang tidak diperlukan di `opencode.json`
2. Set `"enabled": false` untuk MCP yang berat
3. Atau tambah timeout di Nimbalyst (jika ada opsi)

### Masalah: Provider error di Nimbalyst
**Penyebab:** Nimbalyst tidak membaca auth.json OpenCode
**Solusi:**
- Pastikan env var `OPENCODE_CONFIG_DIR` pointing ke `C:\Users\USER\.config\opencode`
- Atau set API key langsung di Nimbalyst settings

---

## 📝 Checklist Setup

- [ ] OpenCode terinstall (`opencode --version` works)
- [ ] PATH includes `C:\Users\USER\AppData\Roaming\npm`
- [ ] Auth configured (`opencode auth list` shows providers)
- [ ] Default model set di `opencode.json`
- [ ] Nimbalyst updated ke versi terbaru
- [ ] OpenCode enabled di Nimbalyst Settings → Agent Providers
- [ ] Test session berhasil di Nimbalyst

---

## 🔗 Referensi

| Resource | URL |
|----------|-----|
| OpenCode Docs | https://opencode.ai/docs/ |
| OpenCode ACP | https://opencode.ai/docs/acp/ |
| OpenCode CLI | https://opencode.ai/docs/cli/ |
| OpenCode Server | https://opencode.ai/docs/server/ |
| Nimbalyst Docs | https://docs.nimbalyst.com/ |
| Nimbalyst Alpha Features | https://docs.nimbalyst.com/setup-nimbalyst/alpha-features/ |
| OpenCode GitHub | https://github.com/anomalyco/opencode |
| Nimbalyst GitHub | https://github.com/Nimbalyst/nimbalyst |

---

## 📊 Status Integrasi

| Komponen | Status | Catatan |
|----------|--------|---------|
| OpenCode CLI | ✅ Ready | v terbaru terinstall via npm |
| Auth Providers | ✅ Ready | 12 providers configured |
| MCP Servers | ⚠️ Partial | 16 MCPs, beberapa mungkin lambat |
| Nimbalyst | ✅ Ready | Terinstall di sistem |
| ACP Protocol | ⚠️ Needs Fix | PATH issue - gunakan solusi di atas |
| Integration | 🔴 Blocked | Sampai PATH issue resolved |

---

*Last Updated: 19 Mei 2026*
*Created for: SD Negeri Pasirhalang OpenCode Configuration*
