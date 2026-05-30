---
name: ux-user-flow
description: >-
  PRD to UX Specifications Generator. Mengubah Product Requirements Document (PRD) menjadi UX & UI
  Specifications lengkap termasuk user flow diagrams, information architecture, view specifications,
  interaction patterns, dan design system integration. Output siap digunakan untuk membuat mockup
  di v0.dev, Figma, atau frontend code. Step 2 dari workflow setelah prd-taskmaster.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# UX-User-Flow: PRD to UX Specifications Generator

## Description
Skill ini mengubah **Product Requirements Document (PRD)** menjadi **UX & UI Specifications lengkap** termasuk user flow diagrams, information architecture, view specifications, interaction patterns, dan design system integration. Output siap digunakan untuk membuat mockup/prototype di tools seperti v0.dev, Figma, atau frontend code.

## Triggers
- "Generate user flow from PRD"
- "Buat user flow dari PRD"
- "Create UX specifications from PRD"
- "Generate user-flow.md"
- "Buatkan UX spec dari PRD"
- "Create user journey from requirements"
- "Make user flow diagram from PRD"
- "Generate mockup specs from PRD"

## Workflow Steps

### Step 1: Load Template
Load the prompt template from `Guided-UX-User-Flow.md` file in the same directory as this SKILL.md. Read the full template content.

### Step 2: Minta PRD dari User
Minta user untuk memberikan PRD yang sudah ada. PRD bisa berupa:
- File `.md` atau dokumen PRD yang sudah dibuat sebelumnya
- Paste langsung teks PRD
- Path ke file PRD di project (misal: `.taskmaster/docs/prd.md`)

### Step 3: Guided UX Discovery
Gunakan template Guided-UX-User-Flow.md untuk memandu sesi tanya jawab interaktif dengan user. Fokus pada:
- **Information Architecture** — Struktur halaman, navigasi, layout zones
- **Core User Flows** — User journeys, decision points, error states, flow diagrams (siap untuk Mermaid.js)
- **View Specifications** — Layout kunci, component hierarchy, state transitions (Empty/Loading/Populated/Error)
- **Interaction Patterns** — Input behaviors, feedback mechanisms, micro-interactions
- **Design System Integration** — Component usage, grid layout, spacing
- **Accessibility** — Keyboard nav, screen reader, touch targets, color contrast
- **Technical Implementation Notes** — Component mapping, state management

### Step 4: Generate user-flow.md
Setelah diskusi selesai, generate file **user-flow.md** dengan struktur:

```markdown
# User Flow & UX Specifications

## 1. Information Architecture
- Screen/Page Map with Hierarchy
- Content Grouping & Component Organization
- Navigation Structure & Patterns
- Layout Zones & Content Blocks
- Responsive Behavior Guidelines

## 2. Core User Flows
- Primary User Journeys (Step-by-Step with Screen States)
- Decision Points & UI Branches
- Error States & Recovery Paths
- Flow Diagrams (Mermaid.js format)
- Success Path Visualization

## 3. View Specifications
- Key Screen Layouts
- Component Hierarchies & Nesting
- State Transitions (Empty, Loading, Populated, Error)
- Data Display Patterns
- Content Priority & Visual Hierarchy

## 4. Interaction Patterns
- Input & Control Behaviors
- Feedback Mechanisms
- Transition Animations & Effects
- Micro-interactions & UI Responses
- Gesture Support

## 5. Design System Integration
- Component Usage Guidelines
- Layout Grid Structure
- Spacing Principles
- UI Pattern Consistency

## 6. Accessibility Considerations
- Keyboard Navigation Paths
- Screen Reader Experience
- Touch Target Guidelines
- Color Contrast Requirements
- Focus State Management

## 7. Technical Implementation Notes
- Frontend Component Mapping
- View State Management Approach
- Critical Rendering Considerations
- Performance Optimization Suggestions

## 8. v0.dev / Mockup Prompt
- Design prompt siap pakai untuk tools generate UI
- Layout descriptions, color scheme, typography
- Component library preferences
```

### Step 5: Tanya Lokasi Penyimpanan
Tanya user di mana file `user-flow.md` akan disimpan. Default:
- `docs/user-flow.md`
- `.taskmaster/docs/user-flow.md`
- Atau lokasi kustom sesuai project

### Step 6: Simpan dan Konfirmasi
- Simpan file `user-flow.md` dengan konten lengkap
- Konfirmasi ke user bahwa file sudah dibuat
- Tawarkan untuk generate Mermaid.js flow diagram jika diminta

## Output Files
- `user-flow.md` — Full UX specifications document
- (Opsional) Flow diagrams dalam format Mermaid.js
- (Opsional) v0.dev prompt siap pakai

## Integration Notes
- Skill ini adalah **Step 2** dari workflow: PRD → UX User Flow → Mockup/Prototype
- Output bisa langsung digunakan untuk:
  - Generate frontend code via v0.dev
  - Membuat mockup di Figma
  - Dasar pembuatan component tree untuk developer
  - Sprint planning & estimation
