# Excel Live Editing Skill

## Overview
Skill untuk membaca dan mengedit file Excel yang sedang terbuka di aplikasi Microsoft Excel tanpa menyebabkan file freeze atau hang.

## MCP Configuration

### excel-control (Primary - Windows Live Editing)
- **Package:** `@negokaz/excel-mcp-server`
- **Command:** `npx -y @negokaz/excel-mcp-server`
- **Enabled:** true
- **Features:**
  - Live editing - berinteraksi dengan file Excel yang sedang terbuka
  - Tidak menyebabkan freeze/hang
  - Screen capture dari sheet Excel
  - Read/write values dan formulas

### excel-mcp (Secondary - Python-based)
- **Package:** Python module `excel_mcp`
- **Command:** `C:\Python\Python313\python.exe -m excel_mcp`

## Available Tools

### 1. excel-control_excel_describe_sheets
Deskripsi: List semua sheet dalam workbook
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel

### 2. excel-control_excel_read_sheet
Deskripsi: Baca nilai dari Excel sheet dengan pagination
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `sheetName`: Nama sheet
- `range`: Range cells (opsional, contoh: "A1:C10")
- `showFormula`: Tampilkan formula instead of value (default: false)
- `showStyle`: Tampilkan style info (default: false)

### 3. excel-control_excel_write_to_sheet
Deskripsi: Tulis nilai ke Excel sheet
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `sheetName`: Nama sheet
- `newSheet`: Create new sheet if true, else write to existing
- `range`: Range cells (contoh: "A1:C10")
- `values`: 2D array of values (gunakan "=" untuk formula)

### 4. excel-control_excel_create_table
Deskripsi: Buat table di Excel sheet
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `sheetName`: Nama sheet
- `range`: Range untuk table (contoh: "A1:C10")
- `tableName`: Nama table

### 5. excel-control_excel_copy_sheet
Deskripsi: Copy existing sheet ke sheet baru
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `srcSheetName`: Nama sheet sumber
- `dstSheetName`: Nama sheet tujuan

### 6. excel-control_excel_format_range
Deskripsi: Format cells di Excel
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `sheetName`: Nama sheet
- `range`: Range cells
- `styles`: 2D array of style objects

### 7. excel-control_excel_screen_capture
Deskripsi: [Windows only] Screenshot dari Excel sheet
Arguments:
- `fileAbsolutePath`: Path absolut ke file Excel
- `sheetName`: Nama sheet
- `range`: Range cells (opsional)

## Usage Guidelines

1. **Selalu gunakan excel-control** dulu untuk operasi Excel karena mendukung live editing
2. Jika excel-control tidak tersedia, gunakan excel-mcp sebagai alternatif
3. Untuk file yang sedang terbuka, cukup gunakan path file seperti biasa - MCP akan mengaksesnya langsung tanpa perlu menutup Excel
4. Pagination default: 4000 cells. Gunakan parameter range untuk membatasi output

## Example Workflow

1. User ingin baca data dari file Excel yang sedang terbuka
2. Gunakan `excel-control_excel_describe_sheets` untuk lihat struktur sheet
3. Gunakan `excel-control_excel_read_sheet` untuk baca data
4. Jika perlu modify, gunakan `excel-control_excel_write_to_sheet`