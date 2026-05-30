---
name: prd-generator
description: >-
  Guided Product Requirements Document Creator. Memandu user melalui proses interaktif untuk
  membuat PRD yang komprehensif melalui sesi tanya jawab terstruktur. Step 1 dari workflow:
  PRD -> UX User Flow -> Mockup/Prototype. Output bisa langsung digunakan oleh skill ux-user-flow.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# PRD-Generator: Guided Product Requirements Document Creator

## Description
Skill ini memandu user melalui proses interaktif untuk membuat **Product Requirements Document (PRD)** yang komprehensif melalui sesi tanya jawab terstruktur. Cocok untuk langkah pertama sebelum membuat user flow dan mockup.

## Triggers
- "Create PRD"
- "Generate product requirements"
- "Buat PRD"
- "Create product requirements document"
- "Generate PRD"
- "Buat product requirements"
- "Start product discovery"

## Workflow Steps

### Step 1: Load Template
Load the prompt template from `Guided-PRD-Creation.md` file in the same directory as this SKILL.md.

### Step 2: Minta Brain Dump
Minta user untuk memberikan "brain dump" — ide kasar, masalah yang ingin diselesaikan, target user, dll.

### Step 3: Guided Discovery Questions
Gunakan template untuk memandu tanya jawab interaktif. Areas yang dicakup:
- **Overview** — Visi produk, problem statement
- **Goals & Objectives** — SMART goals, success metrics
- **Target Audience** — User personas, segments
- **User Stories** — Use cases, acceptance criteria
- **Functional Requirements** — Features, capabilities
- **Non-Functional Requirements** — Performance, security, scalability, usability
- **Design Considerations** — UI/UX preferences, platform
- **Success Metrics** — KPIs, OKRs
- **Open Questions** — Risiko, dependencies, future considerations

### Step 4: Generate PRD Document
Setelah diskusi selesai, generate PRD file dengan format markdown terstruktur.

### Step 5: Simpan dan Konfirmasi
Tanya lokasi penyimpanan (default: `.taskmaster/docs/prd.md` atau `docs/prd.md`) dan simpan file.

## Output
- `prd.md` — Product Requirements Document lengkap
- Siap digunakan sebagai input untuk **ux-user-flow** skill

## Integration
- **Step 1** dari workflow: PRD → UX User Flow → Mockup/Prototype
- Output bisa langsung difeed ke skill `ux-user-flow` untuk generate UX specifications
