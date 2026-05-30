# PowerShell script v2 - Fix SiAdmin.xlsm using XML DOM (safe)
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$filePath = "D:\Pasirhalang\Pasirhalang 2026\ASAJ\SiAdmin.xlsm"
$tempZip = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), "SiAdmin_v2.zip")

try {
    Copy-Item $filePath $tempZip -Force
    $zip = [System.IO.Compression.ZipFile]::Open($tempZip, [System.IO.Compression.ZipArchiveMode]::Update)

    # ===================================================================
    # 1. FIX SHARED STRINGS - Proper Case names & tempat lahir
    # ===================================================================
    Write-Host "--- Fixing shared strings ---"
    $ssEntry = $zip.GetEntry("xl/sharedStrings.xml")
    $ssr = New-Object System.IO.StreamReader($ssEntry.Open())
    $ssXml = $ssr.ReadToEnd()
    $ssr.Close()

    # Define fixes: index → new text
    $fixes = @{
        466 = "Bayu Natabuana"      # BAYU NATABUANA
        470 = "Muhamad Andi Phaeza"   # MUHAMAD ANDI PHAEZA
        474 = "Neng Ika"             # NENG IKA
        483 = "Sri Mulyani"          # SRI MULYANI
        282 = "Bandung Barat"        # BANDUNG BARAT (shared by H11,H12,H20)
        507 = "Bandung Barat"        # BAndung Barat (shared by H10,H28)
        508 = "Cianjur"              # CIANJUR (H29)
    }

    # Load shared strings XML
    $ssDoc = New-Object System.Xml.XmlDocument
    $ssDoc.PreserveWhitespace = $true
    $ssDoc.LoadXml($ssXml)

    # Get namespace
    $ns = New-Object System.Xml.XmlNamespaceManager($ssDoc.NameTable)
    $ns.AddNamespace("s", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")

    # Get all <si> elements  
    $siNodes = $ssDoc.SelectNodes("//s:si", $ns)

    foreach ($idx in $fixes.Keys) {
        if ($idx -lt $siNodes.Count) {
            $siNode = $siNodes[$idx]
            $tNode = $siNode.SelectSingleNode("s:t", $ns)
            if ($tNode -ne $null) {
                $oldText = $tNode.InnerText
                $newText = $fixes[$idx]
                $tNode.InnerText = $newText
                Write-Host "  Index $($idx): '$oldText' → '$newText'"
            }
        }
    }

    # Write back
    $ssw = New-Object System.IO.StreamWriter($ssEntry.Open())
    $ssDoc.Save($ssw)
    $ssw.Close()
    Write-Host "Shared strings done."

    # ===================================================================
    # 2. REMOVE ROWS 31-57 FROM SHEET3 (Data Peserta) using XML DOM
    # ===================================================================
    Write-Host "--- Removing rows 31-57 from Data Peserta ---"
    $s3Entry = $zip.GetEntry("xl/worksheets/sheet3.xml")
    $s3r = New-Object System.IO.StreamReader($s3Entry.Open())
    $s3Xml = $s3r.ReadToEnd()
    $s3r.Close()

    $s3Doc = New-Object System.Xml.XmlDocument
    $s3Doc.PreserveWhitespace = $true
    $s3Doc.LoadXml($s3Xml)

    $ns3 = New-Object System.Xml.XmlNamespaceManager($s3Doc.NameTable)
    $ns3.AddNamespace("s", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")
    $ns3.AddNamespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")
    $ns3.AddNamespace("x14ac", "http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac")

    # Find sheetData
    $sheetData = $s3Doc.SelectSingleNode("//s:sheetData", $ns3)
    if ($sheetData -eq $null) { throw "Cannot find sheetData" }

    # Remove rows 57 down to 31 (reverse order to avoid index shifting)
    for ($r = 57; $r -ge 31; $r--) {
        $row = $sheetData.SelectSingleNode("s:row[@r='$r']", $ns3)
        if ($row -ne $null) {
            $sheetData.RemoveChild($row) | Out-Null
        }
    }
    Write-Host "Rows 31-57 removed from DOM."

    # Update dimension
    $dim = $s3Doc.SelectSingleNode("//s:dimension", $ns3)
    if ($dim -ne $null) {
        $dim.SetAttribute("ref", "A1:AA30")
        Write-Host "Dimension updated to A1:AA30"
    }

    # Write back
    $s3w = New-Object System.IO.StreamWriter($s3Entry.Open())
    $s3Doc.Save($s3w)
    $s3w.Close()
    Write-Host "Sheet3 written."

    # ===================================================================
    # 3. UPDATE TABLE1
    # ===================================================================
    Write-Host "--- Updating Table1 ---"
    $t1Entry = $zip.GetEntry("xl/tables/table1.xml")
    $t1r = New-Object System.IO.StreamReader($t1Entry.Open())
    $t1Xml = $t1r.ReadToEnd()
    $t1r.Close()

    $t1Doc = New-Object System.Xml.XmlDocument
    $t1Doc.PreserveWhitespace = $true
    $t1Doc.LoadXml($t1Xml)

    $nsT = New-Object System.Xml.XmlNamespaceManager($t1Doc.NameTable)
    $nsT.AddNamespace("s", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")

    $table = $t1Doc.SelectSingleNode("//s:table", $nsT)
    if ($table -ne $null) {
        $table.SetAttribute("ref", "A8:O30")
        Write-Host "Table ref updated"
        
        # Update autoFilter
        $af = $table.SelectSingleNode("s:autoFilter", $nsT)
        if ($af -ne $null) {
            $af.SetAttribute("ref", "A8:O30")
            Write-Host "AutoFilter ref updated"
        }
    }

    $t1w = New-Object System.IO.StreamWriter($t1Entry.Open())
    $t1Doc.Save($t1w)
    $t1w.Close()
    Write-Host "Table1 done."

    # ===================================================================
    # 4. UPDATE NAMED RANGE IN WORKBOOK
    # ===================================================================
    Write-Host "--- Updating named range DATA ---"
    $wbEntry = $zip.GetEntry("xl/workbook.xml")
    $wbr = New-Object System.IO.StreamReader($wbEntry.Open())
    $wbXml = $wbr.ReadToEnd()
    $wbr.Close()

    $wbDoc = New-Object System.Xml.XmlDocument
    $wbDoc.PreserveWhitespace = $true
    $wbDoc.LoadXml($wbXml)

    $nsW = New-Object System.Xml.XmlNamespaceManager($wbDoc.NameTable)
    $nsW.AddNamespace("s", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")
    $nsW.AddNamespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")

    # Find definedName for DATA
    $dn = $wbDoc.SelectSingleNode("//s:definedName[@name='DATA']", $nsW)
    if ($dn -ne $null) {
        $dn.InnerText = "'Data Peserta'!" + '$A$9:$M$30'
        Write-Host "Named range DATA updated: $($dn.InnerText)"
    }

    $wbw = New-Object System.IO.StreamWriter($wbEntry.Open())
    $wbDoc.Save($wbw)
    $wbw.Close()
    Write-Host "Workbook done."

    # ===================================================================
    # 5. UPDATE VLOOKUP RANGES IN KARTUPESERTA (sheet5)
    # ===================================================================
    Write-Host "--- Updating VLOOKUP ranges in KartuPeserta ---"
    $s5Entry = $zip.GetEntry("xl/worksheets/sheet5.xml")
    $s5r = New-Object System.IO.StreamReader($s5Entry.Open())
    $s5Xml = $s5r.ReadToEnd()
    $s5r.Close()

    # Safe string replacement (not regex)
    $oldVlookup = "'Data Peserta'!" + '$A$9:$L$68'
    $newVlookup = "'Data Peserta'!" + '$A$9:$L$30'
    $s5Xml = $s5Xml.Replace($oldVlookup, $newVlookup)
    Write-Host "VLOOKUP ranges updated"

    $s5w = New-Object System.IO.StreamWriter($s5Entry.Open())
    $s5w.Write($s5Xml)
    $s5w.Close()
    Write-Host "KartuPeserta done."

    # ===================================================================
    # SAVE
    # ===================================================================
    $zip.Dispose()
    Copy-Item $tempZip $filePath -Force
    Remove-Item $tempZip -Force

    Write-Host "============================================"
    Write-Host "ALL FIXES APPLIED SUCCESSFULLY (v2 - XML DOM)"
    Write-Host "============================================"
}
catch {
    Write-Host "ERROR: $_"
    Write-Host $_.ScriptStackTrace
    exit 1
}
