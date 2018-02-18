VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "YearSummary"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Private fSymbol As String
Private fYearlyChange As Double
Private fPercentageChange As Double
Private fVolume As LongLong

Public Sub Init(sheet As Worksheet, row As Long)
    fSymbol = sheet.Cells(row, 9).Value
    fYearlyChange = sheet.Cells(row, 10).Value
    fPercentageChange = sheet.Cells(row, 11).Value
    fVolume = sheet.Cells(row, 12).Value
End Sub

Public Property Get Symbol() As String
    Symbol = fSymbol
End Property
Public Property Get YearlyChange() As Double
    YearlyChange = fYearlysChange
End Property
Public Property Get PercentageChange() As Double
    PercentageChange = fPercentageChange
End Property
Public Property Get Volume() As LongLong
    Volume = fVolume
End Property


