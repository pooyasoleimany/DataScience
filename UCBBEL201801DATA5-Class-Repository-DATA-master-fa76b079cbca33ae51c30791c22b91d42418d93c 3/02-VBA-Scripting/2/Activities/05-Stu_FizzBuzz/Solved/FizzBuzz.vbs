Sub FizzBuzz

    ' Loop through the values in Column 1
    For i = 2 to 100

        num = Cells(i, 1).value
        
        ' Check if the number is divisible by 3 and 5....
        If (Cells(i, 1).value mod 3 = 0 AND Cells(i, 1).value mod 5 = 0) Then

            ' If so print Fizzbuzz
            Cells(i, 2).value = "Fizzbuzz"

        ' Check if the number is divisible by just 3...
        Elseif (Cells(i, 1).value mod 3 = 0) Then

            ' If so print "Fizz"
            Cells(i, 2).value = "Fizz"

        ' Check if the number is divisible by just 5...
        Elseif (Cells(i, 1).value mod 5 = 0) Then

            ' If so print "Buzz"
            Cells(i, 2).value = "Buzz" 

        End If

    Next i

End Sub