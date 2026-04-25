---
name: browser-use
description: "Integrasi dengan Browser Use API untuk otamatisasi browser berbasis AI. Gunakan untuk web scraping, fill formulir otomatis, login ke website, dan automation tugas-tugas di browser. Sangat berguna untuk Dapodik automation, BOS Online, dan administrasi sekolah."
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: browser-automation
  source: browser-use
---

# Browser Use Integration for OpenCode

Skill ini menyediakan integrasi dengan Browser Use API untuk otomatisasi browser berbasis AI. Gununakan skill ini kapan saja user ingin melakukan web automation, scraping, atau berinteraksi dengan website secara otomatis.

## 🚀 Trigger Phrases

Gunakan skill ini ketika user:
- Ingin mengotomatisasi tugas di browser
-Perlu mengekstrak data dari website
- Ingin login ke website tertentu secara otomatis
- Perlu fill formulir di website
- Mention "browser use", "browser automation", "web automation"
- Ingin scraping data dari website
- Ingin mengintegrasikan dengan Dapodik atau website pendidikan

## 📋 Fungsi Utama

### 1. Web Scraping
```python
# Ekstrak data dari website manapun
agent = Agent(task="Find the price of Sony WH-1000XM5", llm=llm)
```

### 2. Form Automation
```python
# Fill formulir secara otomatis
agent = Agent(task="Login to Dapodik with credentials x,y", llm=llm)
```

### 3. Data Extraction
```python
# Ekstrak data terstruktur dari website
agent = Agent(task="Extract all student names from the roster", llm=llm)
```

### 4. Website Navigation
```python
# Navigasi kompleks di website
agent = Agent(task="Go to BOS online and download the report", llm=llm)
```

## 🔧 Konfigurasi Required

### Environment Variables
```bash
# Buat file .env dengan:
BROWSER_USE_API_KEY=your-api-key
```

### Installation
```bash
# Install library Python
pip install browser-use

# Install Playwright browser
playwright install chromium --with-deps
```

## 📱 Use Cases untuk Admin Sekolah

### Dapodik Automation
- Login otomatis ke Dapodik
- Input data peserta didik
- Input data GTK
- Download laporan

### BOS Online
- Akses bos.kemdikbud.go.id
- Download laporan BOS
- Submit laporan realisasi

### Web Scraping
- Ekstrak data dari website sekolah lain
- Compare data antar sekolah
- Riset sekolah lain untuk benchmarking

### Verval PD/GTK
- Navigasi ke portal verval
- Verifikasi data peserta didi
- Verifikasi data guru

## 🎯 Cara Menggunakan dengan OpenCode

### Metode 1: Cloud API (Recommended)
Menggunakan Browser Use Cloud API untuk tugas-tugas kompleks:

```python
import requests

# Setup
BASE_URL = "https://api.browser-use.com"
API_KEY = "your-browser-use-api-key"
headers = {"X-Browser-Use-API-Key": API_KEY}

# Create session
response = requests.post(
    f"{BASE_URL}/v3/sessions.create()",
    json={"task": "Your task here"},
    headers=headers
)
```

### Metode 2: Open Source (Local)
Menggunakan library Python secara lokal:

```python
from browser_use import Agent, Browser
from browser_use.llm.openai.chat import ChatOpenAI

async def main():
    llm = ChatOpenAI(api_key="your-api-key")
    browser = Browser()
    await browser.start()
    
    agent = Agent(browser=browser, llm=llm)
    await agent.run("Your task")
    
    await browser.stop()
```

## 📝 Contoh Task untuk Sekolah

### Contoh 1: Scraping Data Sekolah
```python
task = "Find all SD schools in Bandung Barat Regency with their NPSN"
```

### Contoh 2: Login Dapodik
```python
task = "Navigate to dapodik.kemdikbud.go.id, login with username X and password Y"
```

### Contoh 3: Download Laporan
```python
task = "Go to bos.kemdikbud.go.id, login, navigate to reports, download JAN report"
```

## 🔐 Keamanan

1. **JANGAN pernah** simpan credentials di code
2. Gunakan environment variables untuk secret
3.Jangan gunakan API key di kode yang di-commit ke git
4.Untuk credentials sensitif, gunakan secure vault

## 📚 Referensi

- Dokumentasi lengkap: https://docs.browser-use.com
- Cloud API: https://docs.cloud.browser-use.com
- GitHub: https://github.com/browser-use/browser-use

## 🎓 Learning Resources

Untuk memahami Browser Use lebih dalam:
1. Quick start: docs.browser-use.com/introduction
2. AI Agents: docs.browser-use.com/customize/actor/basics
3. Cloud API: docs.cloud.browser-use.com/guides/overview

## ⚡ Tips dan Best Practices

1. ** Mulai dengan task sederhana** - Lebih mudah debug
2. **Gunakan explicit selectors** - Lebih reliable daripada AI element selection
3. **Handle errors** - Always add try/except untuk edge cases
4. **Logging** - Log setiap step untuk debugging
5. **Rate limiting** - Jangan terlalu cepat, respect website limits

## 🔧 Troubleshooting

### Common Issues

1. **Element not found**
   - Solution: Gunakan lebih specific selector
   - Alternative: Gunakan AI element selection

2. **Rate limiting**
   - Solution: Tambah delay antar actions
   - Alternative: Use proxy

3. **Captcha**
   - Solution: Browser Use punya built-in CAPTCHA solving
   - Alternative: Use stealth browser

4. **Session timeout**
   - Solution: Use `keep_alive=True`
   - Alternative: Re-create session

## 📞 Support

- Documentation: https://docs.browser-use.com
- GitHub Issues: github.com/browser-use/browser-use/issues
- Discord: discord.gg/browser-use

---

**Catatan**: Skill ini menyediakan integration framework. Untuk penggunaan spesifik, sesuaikan dengan kebutuhan tugas. Untuk Dapodik automation конкрет, mungkin perlu custom script karena struktur Dapodik yang spesifik.