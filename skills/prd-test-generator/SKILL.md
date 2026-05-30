---
name: prd-test-generator
description: >-
  Automated test generator from PRD and User-Flow specifications. Reads PRD.md (from prd-taskmaster)
  and user-flow.md (from ux-user-flow skill), then generates, executes, and reports Playwright-based
  automated tests. Outputs test-report.md with detailed results, screenshots, and coverage analysis.
  Use when user requests "generate test", "buat test", "automated testing", "test from PRD",
  "test from user flow", "generate test report", or "run tests from requirements".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
  - Browser
---

# PRD Test Generator

Generate automated Playwright tests from PRD and User-Flow specifications.
AI handles analysis, planning, and judgment; Playwright handles execution.

**Input**: `PRD.md` + `user-flow.md`
**Output**: `test-report.md` + `test-results/` (screenshots, logs)

---

## Prerequisites: Target Aplikasi Harus Berjalan

Sebelum memulai, pastikan target aplikasi bisa diakses:
- **Localhost:** Pastikan server development sedang berjalan (`npm run dev`, `docker-compose up`, dll)
- **Staging/Production:** Pastikan URL bisa diakses dari jaringan saat ini

> 💡 **Tip:** Jika aplikasi belum berjalan, AI akan mencoba mendeteksi dan membantu menjalankannya.

---

## Workflow (8 Steps)

### Step 1: Cari File PRD dan User-Flow

Cari file PRD dan user-flow dengan urutan prioritas berikut:

**PRD:**
1. `.taskmaster/docs/prd.md` (default dari prd-taskmaster)
2. `docs/prd.md`
3. `PRD.md`
4. Path kustom yang diberikan user

**User-Flow:**
1. `.taskmaster/docs/user-flow.md` (default dari ux-user-flow)
2. `docs/user-flow.md`
3. `user-flow.md`
4. Path kustom yang diberikan user

Gunakan `Glob` untuk mencari file-file tersebut.

**Jika tidak ditemukan:** Tanya user lokasi file PRD dan/atau user-flow.

---

### Step 2: Baca & Analisis Dokumen

Baca kedua file menggunakan `Read` tool:

```markdown
# Analisis PRD:
- Fitur-fitur utama (dari Functional Requirements / User Stories)
- Acceptance Criteria per fitur
- Tech stack & environment
- Test scenarios yang tersirat

# Analisis User-Flow:
- User journeys & flow diagrams
- Decision points & branches
- Error states & recovery paths
- View specifications & component states
- Interaction patterns
```

**AI judgment:** Ekstrak test scenarios dari kombinasi PRD + User-Flow.
Buat daftar test cases yang mencakup:

| Tipe Test | Sumber | Contoh |
|-----------|--------|--------|
| **Happy Path** | User-Flow (Primary Journeys) | Login sukses → dashboard |
| **Error Path** | User-Flow (Error States) | Login gagal → error message |
| **Edge Cases** | PRD (Acceptance Criteria) | Empty state, max length |
| **Validation** | PRD (Non-Functional Req) | Response time < 200ms |
| **UI States** | User-Flow (View Specs) | Loading → Empty → Populated → Error |
| **Accessibility** | User-Flow (A11y section) | Keyboard nav, screen reader |

---

### Step 3: Konfirmasi Test Plan ke User

Tampilkan daftar test cases yang akan dibuat. Minta user untuk:

1. **Pilih test cases** yang ingin dijalankan (default: semua)
2. **Pilih environment** target:
   - Localhost (default)
   - Staging URL
   - Production URL
3. **Pilih browser**: Chromium (default), Firefox, WebKit
4. **Headless mode**: Ya (default) / Tidak

Gunakan `AskUserQuestion` untuk konfirmasi.

---

### Step 4: Generate Test Scripts

Buat struktur folder test:
```
test-results/
├── reports/
│   └── test-report.md
├── screenshots/
│   └── [test-name]/
│       ├── step-1-[description].png
│       └── step-2-[description].png
├── videos/
│   └── [test-name].webm
└── logs/
    └── [test-name].log
```

Generate Playwright test scripts berdasarkan test plan. Setiap test case menjadi 1 file `.spec.ts`:

**Template Test Script:**
```typescript
import { test, expect } from '@playwright/test';

test.describe('[Feature Name]', () => {
  
  test('[Test Case Description]', async ({ page }) => {
    // 1. Navigate
    await page.goto('APP_URL');
    
    // 2. Execute flow (dari user-flow steps)
    await page.click('[selector]');
    await page.fill('[selector]', 'value');
    
    // 3. Assert (dari PRD acceptance criteria)
    await expect(page.locator('[selector]')).toBeVisible();
    await expect(page.locator('[selector]')).toContainText('expected');
    
    // 4. Screenshot
    await page.screenshot({ 
      path: `test-results/screenshots/[test-name]/step-final.png`,
      fullPage: true 
    });
  });
  
  test('[Error Path Test]', async ({ page }) => {
    // Invalid input → error message
    await page.goto('APP_URL');
    await page.fill('[selector]', 'invalid-value');
    await page.click('[submit]');
    
    // Assert error state
    await expect(page.locator('[error-selector]')).toBeVisible();
  });
});
```

**Untuk setup Playwright**, buat file `playwright.config.ts` sementara:
```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './test-results/tests',
  timeout: 30000,
  expect: { timeout: 10000 },
  use: {
    baseURL: 'APP_URL',
    headless: HEADLESS_MODE,
    viewport: { width: 1280, height: 720 },
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  reporter: [
    ['list'],
    ['json', { outputFile: 'test-results/reports/results.json' }],
  ],
});
```

**AI judgment:**
- Gunakan selector yang robust (`data-testid` > text > css)
- Tambahkan wait/retry logic untuk dynamic content
- Group test cases per fitur menggunakan `test.describe()`
- Tambahkan test untuk setiap state transition dari user-flow

**Strategi Selector (Prioritas):**
1. `data-testid` — Paling stabil, recommended oleh Playwright
2. `getByRole()` / `getByText()` — Berdasarkan aksesibilitas, bagus untuk A11y
3. `getByPlaceholder()` — Untuk form input
4. `getByLabel()` — Untuk form dengan label
5. CSS selector — Last resort, gunakan yang spesifik

> Jika aplikasi belum punya `data-testid`, AI akan menganalisis DOM untuk menemukan selector terbaik.
> Untuk akurasi maksimal, rekomendasikan user jalankan: `npx playwright codegen <APP_URL>`

---

### Step 5: Install Dependencies & Run Tests

**Cek Playwright sudah terinstall:**
```bash
npx playwright --version 2>&1 || npm install -g @playwright/test
```

**Install dependencies jika perlu:**
```bash
cd test-results && npm init -y && npm install @playwright/test
npx playwright install chromium 2>&1
```

**Run tests:**
```bash
cd test-results && npx playwright test --reporter=json,list 2>&1
```

**Jika ada error**, gunakan AI judgment untuk:
1. Analisis error log
2. Fix selector atau flow yang bermasalah
3. Re-run test yang gagal
4. Catat fix di test-report

---

### Step 6: Generate test-report.md

Parse hasil test dari JSON output dan generate **test-report.md** dengan struktur:

```markdown
# Test Report: [Project Name]

**Generated:** [Date]
**Source:** PRD.md + user-flow.md
**Environment:** [URL]
**Browser:** [Chromium/Firefox/WebKit]
**Total Tests:** [N] | **Passed:** [N] | **Failed:** [N] | **Skipped:** [N]
**Pass Rate:** [XX]%

---

## Summary by Feature

| Feature | Tests | Passed | Failed | Coverage |
|---------|-------|--------|--------|----------|
| [Feature 1] | 5 | 5 | 0 | ✅ 100% |
| [Feature 2] | 3 | 2 | 1 | ⚠️ 67% |

---

## Detailed Results

### ✅ [Test Name] — PASSED
- **Source:** User-Flow: "Primary Login Journey"
- **PRD Reference:** REQ-001: User Authentication
- **Steps:**
  1. Navigate to login page ✅
  2. Enter credentials ✅
  3. Click login button ✅
  4. Verify dashboard visible ✅

### ❌ [Test Name] — FAILED
- **Source:** PRD Acceptance Criteria: "Error message on invalid login"
- **Error:** `TimeoutError: locator('.error-msg') not visible`
- **Screenshot:** `test-results/screenshots/[test-name]/step-2.png`
- **Suggested Fix:** Check CSS selector for error message element

---

## Coverage Analysis

| PRD Requirement | Covered? | Test File |
|-----------------|----------|-----------|
| REQ-001: Login | ✅ | auth.spec.ts |
| REQ-002: 2FA Setup | ✅ | auth.spec.ts |
| REQ-003: Password Reset | ❌ | Not implemented |
| REQ-004: Dashboard | ⚠️ | Partial coverage |

### Untested Requirements (dari PRD):
- [Req Name] — No test generated
- [Req Name] — Skipped by user

---

## Screenshots & Artifacts

| Test | Screenshot | Video | Log |
|------|-----------|-------|-----|
| Login Success | [View](screenshots/login/step-final.png) | [View](videos/login.webm) | [View](logs/login.log) |
| Login Error | [View](screenshots/login-error/step-final.png) | [View](videos/login-error.webm) | [View](logs/login-error.log) |

---

## Recommendations

1. **[Issue]**: [Description and suggested fix]
2. **[Gap]**: [Missing test coverage and suggestion]
3. **[Improvement]**: [Performance/UX suggestion based on test results]
```

---

### Step 7: Tanya Aksi Selanjutnya

Setelah test-report.md selesai, tanya user:

1. **Lihat report** — Tampilkan summary
2. **Re-run failed tests** — Loop ke Step 5 dengan fix
3. **Save report** — Simpan ke lokasi permanen:
   - `docs/test-report.md`
   - `.taskmaster/docs/test-report.md`
   - Atau path kustom
4. **Add to CI/CD** — Generate GitHub Actions workflow
5. **Exit**

---

### Step 8: Generate CI/CD Workflow (Opsional)

Jika user memilih, generate file `.github/workflows/test.yml`:

```yaml
name: PRD-Based Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      
      - name: Install dependencies
        run: |
          cd test-results
          npm ci
          npx playwright install chromium
      
      - name: Run tests
        run: |
          cd test-results
          npx playwright test --reporter=json
      
      - name: Generate Test Report
        run: |
          # Generate markdown report from JSON
          node -e "
            const fs = require('fs');
            const data = JSON.parse(fs.readFileSync('test-results/reports/results.json'));
            // Generate markdown...
            fs.writeFileSync('test-results/reports/test-report.md', markdown);
          "
      
      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: test-results/reports/
```

---

## MCP Integration

Skill ini bisa menggunakan **Playwright MCP Server** (`microsoft/playwright-mcp`) sebagai alternatif eksekusi test secara interaktif:

| Method | Kelebihan | Kekurangan |
|--------|-----------|------------|
| **Static Script** (default) | Cepat, reproducible, untuk CI/CD | Kurang fleksibel untuk debugging |
| **Playwright MCP** | Interaktif, AI bisa lihat langsung DOM, self-healing | Lebih lambat, perlu koneksi MCP |

**Cara pakai Playwright MCP:**
1. Pastikan MCP server terinstall: `claude mcp add playwright npx @playwright/mcp@latest`
2. AI akan menggunakan browser secara real-time untuk:
   - Mengeksplorasi halaman dan menemukan selector akurat
   - Menjalankan test step-by-step dengan observasi langsung
   - Self-healing jika selector berubah

---

## Tips

- Semakin detail PRD dan user-flow, semakin akurat test yang dihasilkan
- Gunakan `data-testid` attribute di aplikasi untuk selector yang stabil
- Untuk aplikasi yang belum punya test-id, AI akan menggunakan text-based selectors
- Test pertama kali mungkin perlu beberapa iterasi untuk stabil
- Hasil test-report.md bisa langsung di-commit ke repo sebagai dokumentasi
- **Untuk Codebuff/Codebuff:** Skill ini perlu di-load secara eksplisit dengan `/skill prd-test-generator` pada sesi baru jika belum terdaftar di pre-loaded list

## Integration

Skill ini adalah **Step 3** dari workflow lengkap:
1. `prd-taskmaster` → Generate `PRD.md`
2. `ux-user-flow` → Generate `user-flow.md`
3. **`prd-test-generator`** → Generate & run tests → `test-report.md` ✅
