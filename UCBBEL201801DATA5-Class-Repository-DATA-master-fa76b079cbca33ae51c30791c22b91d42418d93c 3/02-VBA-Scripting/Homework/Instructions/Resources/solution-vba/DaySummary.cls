VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "DaySummary"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Private fSymbol As String
Private fDate As Long
Private fOpenPrice As Double
Private fHigh As Double
Private fLow As Double
Private fClosePrice As Double
Private fVolume As Long

Public Sub Init(sheet As Worksheet, row As Long)
    fSymbol = sheet.Cells(row, 1).Value
    fDate = sheet.Cells(row, 2).Value
    fOpenPrice = sheet.Cells(row, 3).Value
    fHigh = sheet.Cells(row, 4).Value
    fLow = sheet.Cells(row, 5).Value
    fClosePrice = sheet.Cells(row, 6).Value
    fVolume = sheet.Cells(row, 7).Value
End Sub

Public Property Get Symbol() As String
    Symbol = fSymbol
End Property
Public Property Get TheDate() As Long
    TheDate = fDate
End Property
Public Property Get OpenPrice() As Double
    OpenPrice = fOpenPrice
End Property
Public Property Get High() As Double
    High = fHigh
End Property
Public Property Get Low() As Double
    Low = fLow
End Property
Public Property Get ClosePrice() As Double
    ClosePrice = fClosePrice
End Property
Public Property Get Volume() As Long
    Volume = fVolume
End Property

