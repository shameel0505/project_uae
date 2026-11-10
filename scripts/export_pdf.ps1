$ppt = New-Object -ComObject PowerPoint.Application
$pptPath = "C:\Users\m.shameel\Downloads\project_uae\Nabat_BioDrop_Technical_Proposal.pptx"
$pdfPath = "C:\Users\m.shameel\Downloads\project_uae\Nabat_BioDrop_Technical_Proposal.pdf"
$pres = $ppt.Presentations.Open($pptPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
$pres.SaveAs($pdfPath, 32)
$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
Get-Item $pdfPath | Select-Object Name, Length, LastWriteTime
