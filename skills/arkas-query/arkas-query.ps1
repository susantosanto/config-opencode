#!/usr/bin/env pwsh
<#
.SYNOPSIS
    ARKAS SQLCipher Query Tool - Wrapper untuk sqlcipher.exe
.DESCRIPTION
    Query database ARKAS (SQLCipher) tanpa perlu input PRAGMA key setiap kali.
.EXAMPLE
    .\arkas-query.ps1 tables
    .\arkas-query.ps1 schema kas_umum
    .\arkas-query.ps1 query "SELECT * FROM kas_umum LIMIT 10"
    .\arkas-query.ps1 query "SELECT * FROM anggaran" --export
    .\arkas-query.ps1 sekolah
    .\arkas-query.ps1 anggaran
    .\arkas-query.ps1 interactive
#>

param(
    [Parameter(Position=0)]
    [string]$Command,

    [Parameter(Position=1)]
    [string]$Argument,

    [switch]$Export,
    [string]$Output,
    [switch]$Help
)

# ─── Konfigurasi ──────────────────────────────────────
$SQLCIPHER = "$env:USERPROFILE\sqlcipher.exe"
$CONFIG = "$env:USERPROFILE\.config\opencode\arkas_config.json"
$EXPORT_DIR = "$env:USERPROFILE\Documents\arkas_analysis\exports"

# Load config
if (Test-Path $CONFIG) {
    $cfg = Get-Content $CONFIG | ConvertFrom-Json
    $DB_PATH = $cfg.arkas.db_path
    $DB_KEY = $cfg.arkas.key
    $SEKOLAH = $cfg.arkas.sekolah
    $NPSN = $cfg.arkas.npsn
} else {
    $DB_PATH = "$env:USERPROFILE\AppData\Roaming\Arkas\arkas.db"
    $DB_KEY = "K3md1kbudRIS3n4yan"
    $SEKOLAH = "Unknown"
    $NPSN = "Unknown"
}

# ─── Fungsi ───────────────────────────────────────────
function Show-Help {
    Write-Host @"
╔══════════════════════════════════════════════════════════╗
║         ARKAS SQLCipher Query Tool v1.0                 ║
║         Database: $SEKOLAH              ║
╚══════════════════════════════════════════════════════════╝

PERINTAH:
  tables                  Daftar semua tabel
  schema [nama_tabel]     Lihat struktur tabel
  query "SQL"             Jalankan SQL query
  query "SQL" --export    Query + export ke Excel
  sekolah                 Info profil sekolah
  anggaran [tahun]        Ringkasan anggaran
  triggers                Daftar trigger
  interactive             Masuk mode interaktif
  backup [nama_file]      Backup database

CONTOH:
  .\arkas-query.ps1 tables
  .\arkas-query.ps1 schema kas_umum
  .\arkas-query.ps1 query "SELECT * FROM kas_umum WHERE soft_delete=0 LIMIT 10"
  .\arkas-query.ps1 query "SELECT * FROM anggaran" --export
  .\arkas-query.ps1 sekolah
  .\arkas-query.ps1 anggaran 2026
  .\arkas-query.ps1 interactive
"@
}

function Invoke-Sqlcipher {
    param(
        [string]$SqlQuery,
        [string]$Mode = "column",
        [switch]$Headers,
        [string]$OutputFile
    )
    
    # Write SQL to temp file and pipe to sqlcipher
    $tempSql = "$env:TEMP\arkas_temp_$([System.IO.Path]::GetRandomFileName()).sql"
    
    # Build SQL file content
    $content = "PRAGMA key = '$DB_KEY';`n"
    
    if ($Mode) {
        $content += ".mode $Mode`n"
    }
    
    if ($Headers) {
        $content += ".headers on`n"
    }
    
    if ($OutputFile) {
        # Escape backslashes for sqlcipher .output command
        $escapedOutput = $OutputFile.Replace('\', '/')
        $content += ".output $escapedOutput`n"
    }
    
    # Ensure query ends with semicolon
    if (-not $SqlQuery.Trim().EndsWith(';')) {
        $SqlQuery = "$SqlQuery;"
    }
    $content += "$SqlQuery`n"
    $content += ".quit`n"
    
    Set-Content -Path $tempSql -Value $content -Encoding UTF8
    
    try {
        # Pipe SQL file content to sqlcipher
        Get-Content $tempSql -Raw | & $SQLCIPHER $DB_PATH 2>&1
    } finally {
        # Clean up temp file
        if (Test-Path $tempSql) {
            Remove-Item $tempSql -Force -ErrorAction SilentlyContinue
        }
    }
}

function Invoke-SqlcipherMulti {
    param(
        [string[]]$Queries,
        [string]$Mode = "column",
        [switch]$Headers
    )
    
    # Write all queries to temp file and pipe to sqlcipher
    $tempSql = "$env:TEMP\arkas_temp_$([System.IO.Path]::GetRandomFileName()).sql"
    
    $content = "PRAGMA key = '$DB_KEY';`n"
    
    if ($Mode) {
        $content += ".mode $Mode`n"
    }
    
    if ($Headers) {
        $content += ".headers on`n"
    }
    
    foreach ($q in $Queries) {
        # Ensure query ends with semicolon
        if (-not $q.Trim().EndsWith(';')) {
            $q = "$q;"
        }
        $content += "$q`n"
    }
    $content += ".quit`n"
    
    Set-Content -Path $tempSql -Value $content -Encoding UTF8
    
    try {
        Get-Content $tempSql -Raw | & $SQLCIPHER $DB_PATH 2>&1
    } finally {
        if (Test-Path $tempSql) {
            Remove-Item $tempSql -Force -ErrorAction SilentlyContinue
        }
    }
}

function Get-Tables {
    $sql = "SELECT name as tabel_name FROM sqlite_master WHERE type='table' ORDER BY name;"
    Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
}

function Get-Schema {
    param([string]$TableName)
    
    if ($TableName) {
        $sql = "PRAGMA table_info($TableName);"
        Write-Host "`n=== Struktur Tabel: $TableName ===" -ForegroundColor Cyan
        Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
    } else {
        Write-Host "`n=== Semua Tabel & Jumlah Baris ===" -ForegroundColor Cyan
        $sql = "SELECT name as tabel, (SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND m.name=name) as info FROM sqlite_master m WHERE type='table' ORDER BY name;"
        Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
    }
}

function Get-Sekolah {
    Write-Host "`n=== Info Sekolah ===" -ForegroundColor Cyan
    Write-Host "Sekolah : $SEKOLAH"
    Write-Host "NPSN    : $NPSN"
    Write-Host ""
    
    $sql = "SELECT * FROM mst_sekolah;"
    Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
}

function Get-Anggaran {
    param([string]$Tahun)
    
    if ($Tahun) {
        $sql = @"
SELECT 
    r.keterangan as rincian,
    a.kode_rekening,
    a.nama_kegiatan,
    a.jumlah,
    a.tahun_anggaran
FROM anggaran a
LEFT JOIN ref_rekening r ON a.kode_rekening = r.kode_rekening
WHERE a.tahun_anggaran = $Tahun AND a.soft_delete = 0
ORDER BY a.kode_rekening;
"@
    } else {
        $sql = @"
SELECT 
    tahun_anggaran,
    COUNT(*) as jumlah_item,
    SUM(jumlah) as total_anggaran
FROM anggaran 
WHERE soft_delete = 0 
GROUP BY tahun_anggaran
ORDER BY tahun_anggaran;
"@
    }
    
    Write-Host "`n=== Ringkasan Anggaran ===" -ForegroundColor Cyan
    Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
}

function Get-Triggers {
    $sql = "SELECT name as trigger_name, tbl_name as tabel, type FROM sqlite_master WHERE type='trigger' ORDER BY name;"
    Write-Host "`n=== Daftar Trigger ===" -ForegroundColor Cyan
    Invoke-Sqlcipher -SqlQuery $sql -Mode "column" -Headers
}

function Invoke-Query {
    param(
        [string]$SqlQuery,
        [switch]$DoExport,
        [string]$ExportPath
    )
    
    if ($DoExport) {
        if (-not $ExportPath) {
            if (-not (Test-Path $EXPORT_DIR)) {
                New-Item -ItemType Directory -Path $EXPORT_DIR -Force | Out-Null
            }
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $ExportPath = "$EXPORT_DIR\arkas_export_$timestamp.xlsx"
        }
        
        # Export ke CSV dulu, lalu convert ke Excel
        $csvPath = [System.IO.Path]::ChangeExtension($ExportPath, ".csv")
        Write-Host "`nExporting ke CSV..." -ForegroundColor Yellow
        Invoke-Sqlcipher -SqlQuery $SqlQuery -Mode "csv" -OutputFile $csvPath
        Write-Host "CSV: $csvPath" -ForegroundColor Green
        
        # Convert ke Excel jika pandas tersedia
        $python = "$env:USERPROFILE\arkas-env\Scripts\python.exe"
        if (Test-Path $python) {
            Write-Host "Converting ke Excel..." -ForegroundColor Yellow
            $pyScript = @"
import pandas as pd
import sys
csv_path = sys.argv[1]
xlsx_path = sys.argv[2]
df = pd.read_csv(csv_path)
df.to_excel(xlsx_path, index=False)
print(f'Excel: {xlsx_path}')
print(f'Baris: {len(df)}')
"@
            $pyFile = "$env:TEMP\convert_excel.py"
            Set-Content -Path $pyFile -Value $pyScript -Encoding UTF8
            & $python $pyFile $csvPath $ExportPath 2>&1
        } else {
            Write-Host "Python tidak ditemukan, CSV saja: $csvPath" -ForegroundColor Yellow
        }
    } else {
        Write-Host ""
        Invoke-Sqlcipher -SqlQuery $SqlQuery -Mode "column" -Headers
    }
}

function Invoke-Interactive {
    Write-Host "`n=== ARKAS Interactive Mode ===" -ForegroundColor Cyan
    Write-Host "Ketik SQL query (akhiri dengan ';')"
    Write-Host "Ketik '.help' untuk bantuan, '.quit' untuk keluar"
    Write-Host ""
    
    $args_ = @(
        $DB_PATH,
        "-cmd", "PRAGMA key = '$DB_KEY';",
        ".mode", "column",
        ".headers", "on"
    )
    
    & $SQLCIPHER @args_
}

function Backup-Database {
    param([string]$BackupName)
    
    if (-not $BackupName) {
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $BackupName = "arkas_backup_$timestamp.db"
    }
    
    $backupPath = "$env:USERPROFILE\Documents\arkas_analysis\$BackupName"
    $backupDir = Split-Path $backupPath -Parent
    
    if (-not (Test-Path $backupDir)) {
        New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    }
    
    Write-Host "`n=== Backup Database ===" -ForegroundColor Cyan
    $sql = ".backup '$backupPath'"
    Invoke-Sqlcipher -SqlQuery $sql
    Write-Host "Backup tersimpan: $backupPath" -ForegroundColor Green
}

# ─── Main ─────────────────────────────────────────────
if ($Help -or -not $Command) {
    Show-Help
    exit 0
}

# Cek sqlcipher exists
if (-not (Test-Path $SQLCIPHER)) {
    Write-Host "ERROR: sqlcipher.exe tidak ditemukan di $SQLCIPHER" -ForegroundColor Red
    exit 1
}

# Cek database exists
if (-not (Test-Path $DB_PATH)) {
    Write-Host "ERROR: Database tidak ditemukan di $DB_PATH" -ForegroundColor Red
    exit 1
}

switch ($Command.ToLower()) {
    "tables" {
        Get-Tables
    }
    "schema" {
        Get-Schema -TableName $Argument
    }
    "query" {
        if (-not $Argument) {
            Write-Host "ERROR: Masukkan SQL query!" -ForegroundColor Red
            Write-Host "Contoh: .\arkas-query.ps1 query `"SELECT * FROM kas_umum LIMIT 10`"" -ForegroundColor Yellow
            exit 1
        }
        Invoke-Query -SqlQuery $Argument -DoExport:$Export -ExportPath:$Output
    }
    "sekolah" {
        Get-Sekolah
    }
    "anggaran" {
        Get-Anggaran -Tahun $Argument
    }
    "triggers" {
        Get-Triggers
    }
    "interactive" {
        Invoke-Interactive
    }
    "backup" {
        Backup-Database -BackupName $Argument
    }
    default {
        Write-Host "ERROR: Perintah tidak dikenal: $Command" -ForegroundColor Red
        Show-Help
        exit 1
    }
}
