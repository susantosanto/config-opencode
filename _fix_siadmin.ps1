# PowerShell script to fix SiAdmin.xlsm
# 1. Remove empty rows 31-57 from Data Peserta
# 2. Fix capitalization (Proper Case) for names and birth places
# 3. Update named range DATA → A9:M30
# 4. Update Table1 ref → A8:O30
# 5. Update KartuPeserta VLOOKUP ranges → A9:L30

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$filePath = "D:\Pasirhalang\Pasirhalang 2026\ASAJ\SiAdmin.xlsm"
$tempDir = [System.IO.Path]::GetTempPath()
$tempZip = [System.IO.Path]::Combine($tempDir, "SiAdmin_temp.zip")

try {
    # Create working copy of the xlsm
    Copy-Item $filePath $tempZip -Force
    
    # Open as ZIP
    $zip = [System.IO.Compression.ZipFile]::Open($tempZip, [System.IO.Compression.ZipArchiveMode]::Update)
    
    # ============== 1. FIX SHARED STRINGS (Proper Case) ==============
    Write-Host "--- Fixing shared strings ---"
    $ssEntry = $zip.GetEntry("xl/sharedStrings.xml")
    $ssr = New-Object System.IO.StreamReader($ssEntry.Open())
    $ssXml = $ssr.ReadToEnd()
    $ssr.Close()
    
    # Read all <si> elements
    $siMatches = [regex]::Matches($ssXml, '<si>.*?</si>', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    $siList = New-Object System.Collections.ArrayList
    foreach ($m in $siMatches) { [void]$siList.Add($m.Value) }
    
    Write-Host "Total shared strings: $($siList.Count)"
    
    # Fix G column names (indices)
    $fixes = @{
        466 = "Bayu Natabuana"     # BAYU NATABUANA
        470 = "Muhamad Andi Phaeza" # MUHAMAD ANDI PHAEZA
        474 = "Neng Ika"            # NENG IKA
        483 = "Sri Mulyani"         # SRI MULYANI
    }
    
    # Fix H column tempat lahir (indices)
    $hFixes = @{
        282 = "Bandung Barat"       # BANDUNG BARAT
        507 = "Bandung Barat"       # BAndung Barat
        508 = "Cianjur"             # CIANJUR
    }
    
    $fixes = $fixes + $hFixes
    
    foreach ($idx in $fixes.Keys) {
        if ($idx -lt $siList.Count) {
            $oldSi = $siList[$idx]
            $newText = $fixes[$idx]
            # Replace content inside <t>...</t> but preserve <si> wrapper and any other child elements
            $newSi = $oldSi -replace '(?<=<t[^>]*>).*?(?=</t>)', $newText
            $siList[$idx] = $newSi
            Write-Host "  Fixed index $($idx): $newText"
        }
    }
    
    # Write the modified string items back
    $newSsXml = $ssXml
    # Replace in reverse order to not mess up positions
    for ($i = $siList.Count - 1; $i -ge 0; $i--) {
        $newSsXml = $newSsXml.Remove($siMatches[$i].Index, $siMatches[$i].Length).Insert($siMatches[$i].Index, $siList[$i])
    }
    
    # Write back to ZIP
    $ssWriter = New-Object System.IO.StreamWriter($ssEntry.Open())
    $ssWriter.Write($newSsXml)
    $ssWriter.Close()
    Write-Host "Shared strings written"
    
    # ============== 2. REMOVE ROWS 31-57 FROM SHEET3 ==============
    Write-Host "--- Removing rows 31-57 from Data Peserta ---"
    $s3Entry = $zip.GetEntry("xl/worksheets/sheet3.xml")
    $s3r = New-Object System.IO.StreamReader($s3Entry.Open())
    $s3Xml = $s3r.ReadToEnd()
    $s3r.Close()
    
    # Remove row elements r=31 through r=57
    for ($r = 31; $r -le 57; $r++) {
        $pattern = "(?s)<row r=`"$r`"[^>]*>.*?</row>"
        $s3Xml = $s3Xml -replace $pattern, ""
    }
    
    # Clean up extra whitespace/newlines from removals
    $s3Xml = $s3Xml -replace '(?m)^\s*\n', ''
    
    # Update dimension from A1:AA140 to A1:AA30
    $s3Xml = $s3Xml -replace 'dimension ref="A1:AA140"', 'dimension ref="A1:AA30"'
    
    $s3Writer = New-Object System.IO.StreamWriter($s3Entry.Open())
    $s3Writer.Write($s3Xml)
    $s3Writer.Close()
    Write-Host "Rows 31-57 removed, dimension updated"
    
    # ============== 3. UPDATE TABLE1 ==============
    Write-Host "--- Updating Table1 ---"
    $t1Entry = $zip.GetEntry("xl/tables/table1.xml")
    $t1r = New-Object System.IO.StreamReader($t1Entry.Open())
    $t1Xml = $t1r.ReadToEnd()
    $t1r.Close()
    
    $t1Xml = $t1Xml -replace 'ref="A8:O140"', 'ref="A8:O30"'
    $t1Xml = $t1Xml -replace '(?<=<autoFilter[^>]*)ref="A8:O140"', 'ref="A8:O30"'
    
    # Fix - both ref="A8:O140" and autoFilter ref
    # Simpler: just replace all A8:O140
    $t1Xml = $t1Xml.Replace('A8:O140', 'A8:O30')
    
    $t1Writer = New-Object System.IO.StreamWriter($t1Entry.Open())
    $t1Writer.Write($t1Xml)
    $t1Writer.Close()
    Write-Host "Table1 updated to A8:O30"
    
    # ============== 4. UPDATE NAMED RANGE IN WORKBOOK ==============
    Write-Host "--- Updating named range DATA ---"
    $wbEntry = $zip.GetEntry("xl/workbook.xml")
    $wbr = New-Object System.IO.StreamReader($wbEntry.Open())
    $wbXml = $wbr.ReadToEnd()
    $wbr.Close()
    
    $oldRange = "'Data Peserta'!" + '$A$9:$M$68'
    $newRange = "'Data Peserta'!" + '$A$9:$M$30'
    $wbXml = $wbXml.Replace($oldRange, $newRange)
    
    $wbWriter = New-Object System.IO.StreamWriter($wbEntry.Open())
    $wbWriter.Write($wbXml)
    $wbWriter.Close()
    Write-Host "Named range DATA updated to A9:M30"
    
    # ============== 5. UPDATE VLOOKUP RANGES IN KARTUPESERTA ==============
    Write-Host "--- Updating VLOOKUP ranges in KartuPeserta ---"
    $s5Entry = $zip.GetEntry("xl/worksheets/sheet5.xml")
    $s5r = New-Object System.IO.StreamReader($s5Entry.Open())
    $s5Xml = $s5r.ReadToEnd()
    $s5r.Close()
    
    # Replace all hardcoded VLOOKUP range references
    $s5Xml = $s5Xml.Replace("'Data Peserta'!`$A`$9:`$L`$68", "'Data Peserta'!`$A`$9:`$L`$30")
    
    $s5Writer = New-Object System.IO.StreamWriter($s5Entry.Open())
    $s5Writer.Write($s5Xml)
    $s5Writer.Close()
    Write-Host "VLOOKUP ranges updated to A9:L30"
    
    # ============== SAVE ==============
    $zip.Dispose()
    
    # Copy back to original
    Copy-Item $tempZip $filePath -Force
    Remove-Item $tempZip -Force
    
    Write-Host "========================================="
    Write-Host "ALL FIXES APPLIED SUCCESSFULLY!"
    Write-Host "========================================="
}
catch {
    Write-Host "ERROR: $_"
    Write-Host $_.ScriptStackTrace
    exit 1
}
