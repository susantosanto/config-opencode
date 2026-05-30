---
name: design-md
description: "Google Labs DESIGN.md format — spesifikasi design system untuk coding agents. Gunakan saat membangun frontend, mendesain UI, atau ingin memberi agent pemahaman visual identity yang persisten via file DESIGN.md. Integrasi dengan awesome-design-md untuk template brand."
---

# Skill: DESIGN.md — Google Labs Design System Format

## Ringkasan

`DESIGN.md` adalah format spesifikasi dari Google Labs untuk mendeskripsikan visual identity ke coding agents. Menggabungkan **YAML front matter** (token desain machine-readable) dengan **markdown prose** (rationale desain human-readable).

**Repo:** [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)  
**Spec lengkap:** `docs/spec.md` di repo  
**CLI:** `@google/design.md` (npm)

---

## Struktur File DESIGN.md

```
---
name: <nama-design-system>
colors:
  primary: "#HEX"
  secondary: "#HEX"
  ...
typography:
  h1:
    fontFamily: ...
    fontSize: ...
    ...
rounded:
  sm: 4px
  md: 8px
  ...
spacing:
  sm: 8px
  md: 16px
  ...
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: ...
    ...
---

## Overview

Deskripsi holistik look & feel.

## Colors

Penjelasan palet warna.

## Typography

Penjelasan tipografi.

## Layout

Layout & spacing strategy.

## Elevation & Depth

Visual hierarchy / shadows.

## Shapes

Corner radius, bentuk elemen.

## Components

Style guidance untuk atom components.

## Do's and Don'ts

Panduan dan common pitfalls.
```

### Token Schema Lengkap

```yaml
version: <string>           # optional, "alpha"
name: <string>
description: <string>       # optional
colors:
  <token-name>: <Color>     # "#HEX" (sRGB)
typography:
  <token-name>:
    fontFamily: <string>
    fontSize: <Dimension>    # "16px", "1rem"
    fontWeight: <number>     # 400, 600, 700
    lineHeight: <Dimension|number>  # "24px" atau 1.6
    letterSpacing: <Dimension>      # "-0.02em"
    fontFeature: <string>    # optional
    fontVariation: <string>  # optional
rounded:
  <scale-level>: <Dimension> # "sm: 4px", "md: 8px"
spacing:
  <scale-level>: <Dimension|number>
components:
  <component-name>:
    backgroundColor: <Color|reference>
    textColor: <Color|reference>
    typography: <Typography|reference>
    rounded: <Dimension|reference>
    padding: <Dimension>
    size: <Dimension>
    height: <Dimension>
    width: <Dimension>
```

**Token Reference:** `{colors.primary}`, `{typography.h1}`, `{rounded.md}`  
**Dimension:** number + unit (`px`, `em`, `rem`)

### Aturan Section Order

| # | Section | Alias |
|---|---------|-------|
| 1 | Overview | Brand & Style |
| 2 | Colors | |
| 3 | Typography | |
| 4 | Layout | Layout & Spacing |
| 5 | Elevation & Depth | Elevation |
| 6 | Shapes | |
| 7 | Components | |
| 8 | Do's and Don'ts | |

Sections boleh di-omit, tapi yang muncul HARUS dalam urutan ini.

---

## CLI Reference (`@google/design.md`)

### Install

```bash
npm install @google/design.md
# Windows: npm install "@google/design.md"
# Atau langsung via npx:
npx @google/design.md lint DESIGN.md
```

**⚠️ Catatan Windows:** Gunakan `designmd` (tanpa `.md`) sebagai alias di package.json scripts karena `.md` di bin name membingungkan Windows.

### Commands

| Perintah | Fungsi |
|----------|--------|
| `designmd lint DESIGN.md` | Validasi struktur DESIGN.md |
| `designmd diff BEFORE.md AFTER.md` | Bandingkan 2 versi DESIGN.md |
| `designmd export --format json-tailwind DESIGN.md` | Export ke Tailwind v3 config |
| `designmd export --format css-tailwind DESIGN.md` | Export ke Tailwind v4 `@theme` |
| `designmd export --format dtcg DESIGN.md` | Export ke W3C DTCG tokens.json |
| `designmd spec` | Output format spec (berguna untuk agent prompt) |

### Linting Rules (7 rules)

| Rule | Severity | Cek |
|------|----------|-----|
| `broken-ref` | ❌ error | Token reference tidak resolve |
| `missing-primary` | ⚠️ warning | Tidak ada `primary` color |
| `contrast-ratio` | ⚠️ warning | Kontras WCAG AA < 4.5:1 |
| `orphaned-tokens` | ⚠️ warning | Color token tidak dipakai komponen |
| `token-summary` | ℹ️ info | Summary jumlah token |
| `missing-sections` | ℹ️ info | Section opsional tidak ada |
| `missing-typography` | ⚠️ warning | Warna ada tapi typography tidak |
| `section-order` | ⚠️ warning | Urutan section salah |

### Export Examples

```bash
# Tailwind v3
designmd export --format json-tailwind DESIGN.md > tailwind.theme.json

# Tailwind v4
designmd export --format css-tailwind DESIGN.md > theme.css

# W3C Design Tokens
designmd export --format dtcg DESIGN.md > tokens.json
```

---

## Integrasi dengan awesome-design-md

`awesome-design-md` (dari VoltAgent) menyediakan template DESIGN.md untuk brand terkenal. Skill ini komplementer:

| Skill | Fungsi |
|-------|--------|
| `awesome-design-md` | Install template DESIGN.md brand (Stripe, Vercel, dll) |
| `design-md` **(ini)** | Validasi, diff, export DESIGN.md + paham format spec |

**Alur kerja:**
1. `awesome-design-md` → `install stripe` → dapat `DESIGN.md`
2. `design-md` → `lint DESIGN.md` → validasi struktur
3. `design-md` → `export --format css-tailwind DESIGN.md` → siap pakai

---

## Cara Pakai di Agent Prompt

Saat mendesain UI, agent perlu:
1. **Cari atau buat** file `DESIGN.md` di root proyek
2. **Baca token** dari YAML front matter untuk nilai exact
3. **Baca prose** untuk rationale desain dan konteks
4. **Terapkan** secara konsisten di semua komponen

### Contoh Prompt ke Agent:
> "Baca DESIGN.md di proyek ini, lalu buat komponen Login card yang sesuai dengan design system di sana. Gunakan token warna, tipografi, dan spacing yang sudah didefinisikan."

---

*Sumber: [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)*  
*Lisensi: Apache-2.0*
