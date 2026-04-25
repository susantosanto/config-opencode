#!/usr/bin/env python3
"""
Dapodik Login Automation dengan Browser Use
============================================
Script untuk login otomatis ke aplikasi Dapodik Web Service

Usage:
    python dapodik_login.py [username] [password]

Contoh:
    python dapodik_login.py operator@sekolah.com password123
"""

import asyncio
import sys
from browser_use import Agent, Browser
from browser_use.llm.openai.chat import ChatOpenAI

# ============================================================
# KONFIGURASI - GANTI DENGAN CREDENTIALS ANDA
# ============================================================
DAPODIK_URL = "http://localhost:5774"
USERNAME = "sdnpasirhalang.cikalong@gmail.com"  # <- ISI USERNAME DAPODIK ANDA
PASSWORD = "123Unpas!!!"  # <- ISI PASSWORD DAPODIK ANDA
SEMESTER = "20252"  # 2025/2026 Genap

# ============================================================
# BROWSER USE DENGAN CLOUD API (GUNAKAN API KEY ANDA)
# ============================================================
BROWSER_USE_API_KEY = "bu_LhIG78MIQESjvwaDKcRpcfPdQAqBcjC7wnUpSyJrSLM"


async def login_dapodik():
    """Login ke Dapodik menggunakan Browser Use Cloud"""
    
    print("🚀 Memulai Browser Use untuk login Dapodik...")
    print(f"   URL: {DAPODIK_URL}")
    
    # Initialize Browser Use Cloud
    from browser_use.llm.openai.chat import ChatOpenAI
    from browser_use import Agent
    
    # Setup LLM dengan OpenAI (bisa diganti dengan model lain)
    llm = ChatOpenAI(
        api_key="sk-"  # Diisi dengan API key OpenAI jika tidak pakai cloud
    )
    
    # task untuk login ke Dapodik
    task = f"""Buka {DAPODK_URL}, lalu:
1. Tunggu halaman login loaded
2. Cari input field dengan name="username", isi dengan: {USERNAME}
3. Cari input field dengan name="password", isi dengan: {PASSWORD}
4. Pilih semester dengan name="semester_id", pilih option value={SEMESTER}
5. Klik button "Masuk" untuk submit form
6. Tunggu hingga halaman berubah atau ada pesan error
7. Ambil screenshot sebagai bukti login
8. Berikan status: berhasil atau gagal beserta reasonnya
"""
    
    print(f"\n📋 Task: {task}")
    print("\n⏳ Menjalankan browser automation...")
    
    # Jalankan agent
    agent = Agent(
        task=task,
        llm=llm,
    )
    
    result = await agent.run()
    
    print("\n" + "="*50)
    print("📊 HASIL LOGIN:")
    print("="*50)
    print(result)
    print("="*50)
    
    return result


async def login_dapodik_simple():
    """Versi sederhana tanpe LLM - langsung fill form"""
    
    if not USERNAME or not PASSWORD:
        print("❌ ERROR: Username dan Password harus diisi!")
        print("   Usage: python dapodik_login.py [username] [password]")
        sys.exit(1)
    
    print(f"🚀 Login ke Dapodik: {DAPODIK_URL}")
    print(f"   Username: {USERNAME}")
    print(f"   Semester: {SEMESTER}")
    
    # Initialize browser
    browser = Browser()
    await browser.start()
    
    try:
        # Buka halaman Dapodik
        page = await browser.new_page(DAPODIK_URL)
        print("📄 Halaman login dibuka...")
        
        # Tunggu form ready
        await page.wait_for_selector('input[name="username"]', timeout=10000)
        
        # Fill username
        username_input = await page.get_element('input[name="username"]')
        await username_input.fill(USERNAME)
        print(f"✅ Username diisi: {USERNAME}")
        
        # Fill password  
        password_input = await page.get_element('input[name="password"]')
        await password_input.fill(PASSWORD)
        print("✅ Password diisi")
        
        # Pilih semester
        semester_select = await page.get_element('select[name="semester_id"]')
        await semester_select.fill(SEMESTER)
        print(f"✅ Semester dipilih: {SEMESTER}")
        
        # Klik tombol masuk
        masuk_btn = await page.get_element('button:has-text("Masuk")')
        await masuk_btn.click()
        print("🔄 Klik tombol Masuk...")
        
        # Tunggu response
        await page.wait_for_load_state("networkidle")
        
        # Ambil screenshot
        await page.screenshot("dapodik_login_result.png")
        print("📸 Screenshot disimpan: dapodik_login_result.png")
        
        # Cek URL sekarang - kalau masih di halaman login = gagal
        current_url = page.url
        if "login" in current_url.lower() or current_url == DAPODIK_URL + "/":
            print("❌ LOGIN GAGAL! Masih di halaman login")
        else:
            print(f"✅ LOGIN BERHASIL! Saat ini di: {current_url}")
        
        # Ambil info halaman
        title = await page.title()
        print(f"   Page title: {title}")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        
    finally:
        await browser.stop()


# ============================================================
# VERSI LANGSUNG DENGAN PLAYWRIGHT TANPA BROWSER USE
# ============================================================
async def login_dapodik_playwright():
    """Versi simpel langsung dengan Playwright - tidak perlu OpenAI API"""
    
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("📦 Install playwright dulu:")
        print("   pip install playwright")
        print("   playwright install chromium")
        sys.exit(1)
    
    if not USERNAME or not PASSWORD:
        print("❌ ERROR: Username dan Password harus diisi!")
        sys.exit(1)
    
    print(f"\n🚀 Login ke Dapodik (Playwright)")
    print(f"   User: {USERNAME}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 720})
        
        # Buka Dapodik
        await page.goto(DAPODIK_URL)
        print("📄 Halaman login dibuka...")
        
        # Fill username
        await page.fill('input[name="username"]', USERNAME)
        print("✅ Username diisi")
        
        # Fill password
        await page.fill('input[name="password"]', PASSWORD)
        print("✅ Password diisi")
        
        # Select semester
        await page.select_option('select[name="semester_id"]', SEMESTER)
        print(f"✅ Semester dipilih")
        
        # Click login
        await page.click('button:has-text("Masuk")')
        print("🔄 Klik Masuk...")
        
        # Wait
        await page.wait_for_load_state("networkidle", timeout=15000)
        
        # Screenshot
        await page.screenshot(path="dapodik_login.png")
        print("📸 Screenshot: dapodik_login.png")
        
        # Check result
        url = page.url
        print(f"\n   URL sekarang: {url}")
        
        if "login" in url.lower():
            print("❌ LOGIN GAGAL")
        else:
            print("✅ LOGIN BERHASIL!")
        
        await browser.close()


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) >= 3:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
        print(f"📝 Args: username={USERNAME}, password={'*'*len(PASSWORD)}")
    elif len(sys.argv) == 2:
        print("Usage: python dapodik_login.py [username] [password]")
        sys.exit(1)
    
    # Jalankan - Playwright adalah yang paling reliable
    asyncio.run(login_dapodik_playwright())
    print(f"   USERNAME: {USERNAME or '(belum ada)'}")
    print(f"   PASSWORD: {PASSWORD and '(sudah ada)' or '(belum ada)'}")
    print("\n✅ Script siap! Jalankan dengan:")
    print(f"   python {__file__} [username] [password]")