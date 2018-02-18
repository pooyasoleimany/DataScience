Attribute VB_Name = "MarketDataAnalyzer"
Function CreateDaySummary(sheet As Worksheet, row As Long) As DaySummary
    Dim summary As DaySummary
    Set summary = New DaySummary
    Call summary.Init(sheet, row)
    Set CreateDaySummary = summary
End Function
Function CreateYearSummary(sheet As Worksheet, row As Long) As YearSummary
    Dim summary As YearSummary
    Set summary = New YearSummary
    Call summary.Init(sheet, row)
    Set CreateYearSummary = summary
End Function
Sub PrintSummaryHeader(sheet As Worksheet)
    sheet.Range("I1").Value = "Ticker"
    sheet.Range("J1").Value = "Yearly Change"
    sheet.Range("K1").Value = "Percentage Change"
    sheet.Range("L1").Value = "Total Stock Volume"
End Sub
Sub PrintSummary(sheet As Worksheet, firstSummary As DaySummary, lastSummary As DaySummary, totalVolume As LongLong, row As Long)
    Dim change As Double
    change = lastSummary.ClosePrice - firstSummary.OpenPrice
    sheet.Cells(row, 9).Value = firstSummary.Symbol
    sheet.Cells(row, 10).Value = change
    sheet.Cells(row, 11).Value = change / firstSummary.OpenPrice
    sheet.Cells(row, 12).Value = totalVolume
End Sub
Function GetLastRow(sheet As Worksheet, column As Integer) As Long
    GetLastRow = sheet.Cells(Rows.Count, column).End(xlUp).row
End Function
Sub CreateTickerSummary(sheet As Worksheet)
    Dim firstRow As Long
    Dim lastRow As Long
    Dim row As Long
    Dim summaryRow As Long
    firstRow = 2
    lastRow = GetLastRow(sheet, 1) + 1
    summaryRow = firstRow
    Dim firstSummary As DaySummary
    Dim previousSummary As DaySummary
    Dim summary As DaySummary
    Dim totalVolume As LongLong
    Set previousSummary = CreateDaySummary(sheet, firstRow)
    Set firstSummary = previousSummary
    totalVolume = firstSummary.Volume
    For row = firstRow + 1 To lastRow
        Set summary = CreateDaySummary(sheet, row)
        If summary.Symbol = previousSummary.Symbol Then
            totalVolume = totalVolume + summary.Volume
            Set previousSummary = summary
        Else
            Call PrintSummary(sheet, firstSummary, previousSummary, totalVolume, summaryRow)
            summaryRow = summaryRow + 1
            Set firstSummary = summary
            totalVolume = firstSummary.Volume
            Set previousSummary = summary
        End If
    Next row
End Sub
Sub FormatPercentageChange(sheet As Worksheet)
    sheet.Range("K2", sheet.Range("K2").End(xlDown)).NumberFormat = "0.00%"
    sheet.Range("Q2:Q3").NumberFormat = "0.00%"
End Sub
Sub Clear(sheet As Worksheet)
    sheet.Columns("I:Z").Delete
End Sub
Sub FormatYearlyChange(sheet As Worksheet)
    For Each cell In sheet.Range("J2", sheet.Range("J2").End(xlDown))
        If cell > 0 Then
            cell.Interior.Color = RGB(0, 255, 0)
        Else
            cell.Interior.Color = RGB(255, 0, 0)
        End If
    Next cell
End Sub
Sub TopPerformerHeader(sheet As Worksheet)
    sheet.Range("P1") = "Ticker"
    sheet.Range("Q1") = "Value"
    sheet.Range("O2") = "Greatest % Increase"
    sheet.Range("O3") = "Greatest % Decrease"
    sheet.Range("O4") = "Greatest Total Volume"
End Sub
Sub TopPerformer(sheet As Worksheet)
    Dim firstRow As Long
    Dim lastRow As Long
    Dim row As Long
    firstRow = 2
    lastRow = GetLastRow(sheet, 9) + 1
    Dim maxVolume As YearSummary
    Dim maxPercentIncrease As YearSummary
    Dim maxPercentDecrease As YearSummary
    Dim summary As YearSummary
    Set summary = CreateYearSummary(sheet, firstRow)
    Set maxVolume = summary
    Set maxPercentIncrease = summary
    Set maxPercentDecrease = summary
    For row = firstRow + 1 To lastRow
        Set summary = CreateYearSummary(sheet, row)
        If summary.PercentageChange > maxPercentIncrease.PercentageChange Then
            Set maxPercentIncrease = summary
        End If
        If summary.PercentageChange < maxPercentDecrease.PercentageChange Then
            Set maxPercentDecrease = summary
        End If
        If summary.Volume > maxVolume.Volume Then
            Set maxVolume = summary
        End If
    Next row
    sheet.Range("P2").Value = maxPercentIncrease.Symbol
    sheet.Range("Q2").Value = maxPercentIncrease.PercentageChange
    sheet.Range("P3").Value = maxPercentDecrease.Symbol
    sheet.Range("Q3").Value = maxPercentDecrease.PercentageChange
    sheet.Range("P4").Value = maxVolume.Symbol
    sheet.Range("Q4").Value = maxVolume.Volume
End Sub
Sub FormatColumnSize(sheet As Worksheet)
    sheet.Columns("I:Z").AutoFit
End Sub
Sub TickerSummary(sheet As Worksheet)
    Call PrintSummaryHeader(sheet)
    Call CreateTickerSummary(sheet)
End Sub
Sub TopPerformerSummary(sheet As Worksheet)
    Call PrintSummaryHeader(sheet)
    Call CreateTickerSummary(sheet)
    Call TopPerformerHeader(sheet)
    Call TopPerformer(sheet)
    Call FormatPercentageChange(sheet)
    Call FormatYearlyChange(sheet)
    Call FormatColumnSize(sheet)
End Sub
Sub Format(sheet As Worksheet)
    Call FormatPercentageChange(sheet)
    Call FormatYearlyChange(sheet)
    Call FormatColumnSize(sheet)
End Sub
Sub Test()
    Dim s1 As Worksheet
    For Each s1 In Worksheets
        Call Clear(s1)
    Next s1
    Dim s2 As Worksheet
    For Each s2 In Worksheets
        Call TickerSummary(s2)
    Next s2
    Dim s3 As Worksheet
    For Each s3 In Worksheets
        Call TopPerformerSummary(s3)
    Next s3
    Dim s4 As Worksheet
    For Each s4 In Worksheets
        Call Format(s4)
    Next s4
End Sub
