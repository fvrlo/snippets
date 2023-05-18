%HOTKEY%::
wbk := ComObjGet("C:\Path\To\Workbook.xlsx")
valuable := wbk.Sheets("Sheet Name").Cells(2, 4).Value
SendInput, %valuable%
return