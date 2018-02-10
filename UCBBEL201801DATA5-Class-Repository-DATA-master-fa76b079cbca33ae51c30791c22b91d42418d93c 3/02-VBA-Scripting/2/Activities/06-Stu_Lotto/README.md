# The VBA Lotto

## Instructions

* You are in charge of finding our winners for a local lotto drawing.

  * The results are, in order:

    * First: 3957481
    * Second: 5865187
    * Third: 2817729

  * Create a script that will return those lucky winners and print them on the sheet.

    * For each winner include the following pieces of information:

      * First name
      * Last name
      * The winning number

    * They should be placed in winning order of First, Second, Third.

    * There should also be a message box that congratulates the first place winner.

## Bonus

* There may just be one other winner! The below numbers are Wild Lotto Balls. Whichever comes up first in the list will be the fourth place (runner-up) winner.

  * 2275339
  * 5868182
  * 1841402

## Hint

* Remember to utilize variables to keep your code clean.

* For the bonus, you may need to use `Exit For`




Sub lottery():
Dim winningNumber1 As Long
Dim winningNumber2 As Long
Dim winningNumber3 As Long
Dim winningNumber4(3) As Long
winningNumber1 = 3957481
winningNumber2 = 5865187
winningNumber3 = 2817729
winningNumber4(0) = 2275339
winningNumber4(1) = 5868182
winningNumber4(2) = 1841402
    For i = 2 To 1001
        If Cells(i, 3).Value = winningNumber1 Then
            Range("F2").Value = Cells(i, 1).Value
            Range("G2").Value = Cells(i, 2).Value
            Range("H2").Value = Cells(i, 3).Value
       ElseIf Cells(i, 3).Value = winningNumber2 Then
            Range("F3").Value = Cells(i, 1).Value
            Range("G3").Value = Cells(i, 2).Value
            Range("H3").Value = Cells(i, 3).Value
       ElseIf Cells(i, 3).Value = winningNumber3 Then
            Range("F4").Value = Cells(i, 1).Value
            Range("G4").Value = Cells(i, 2).Value
            Range("H4").Value = Cells(i, 3).Value
       End If
    Next i
    For i = 2 To 1001
        for j = 0 to 2
          If Cells(i, 3).Value = winningNumber4(j) Then
              Range("F5").Value = Cells(i, 1).Value
              Range("G5").Value = Cells(i, 2).Value
              Range("H5").Value = Cells(i, 3).Value
          End If
       next j
    Next i
End Sub
