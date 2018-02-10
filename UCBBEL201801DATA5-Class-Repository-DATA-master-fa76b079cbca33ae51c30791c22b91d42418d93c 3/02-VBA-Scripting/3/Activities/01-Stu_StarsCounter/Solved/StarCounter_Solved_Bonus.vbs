' StarCounter
' 1. Create a nested for loop that iterates through each student.
' 2. For each loop count the number of instances of the word "Full-Star" using a counter
' 3. Save the counter value to the total cell
' 4. BONUS: Instead of hard-coding the last number of the loop, use VBA to determine the last row.
' 5. BONUS: Create two charts:
     ' One to see if there is a relationship between Program type and Rating
     ' One to see if there is a relationship between Date and Rating

Sub StarCounter()

  ' Create a variable to hold the StarCounter. We will repeatedly use this.
  Dim StarCounter As Integer
  
  ' BONUS: Create a varaible to hold the TotalStars. This will keep track of how many stars both programs received
  Dim TotalStars As Integer

  ' BONUS: Initially set TotalStars to 0 since we will be adding total on top of this
  TotalStars = 0
  
  ' Loop through each row
  For i = 2 To 51

    ' Initially set the StarCounter to be 0 for each row
    StarCounter = 0

    ' While in each row, loop through each star column
    For j = 4 To 8

      ' If a column contains the word "Full-Star"...
      If (Cells(i, j).Value = "Full-Star") Then

        ' Add 1 to the StarCounter
        StarCounter = StarCounter + 1

      End If

    Next j

    ' Once we've completed all rows, print the value in the total column
    Cells(i, 9).Value = StarCounter
    
    ' BONUS: Set the value of TotalStars to the previous value plus the value of StarCounter
    TotalStars = TotalStars + StarCounter

  Next i
  
' BONUS: Once both loops have concluded, print the TotalStars value into a cell
Cells(54, 9).Value = TotalStars

End Sub
