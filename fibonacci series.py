Number = int(input("\nPlease Enter the Range : "))

# Initializing First and Second Values
i = 0
First_Value = 0
Second_Value = 1

# Find & Displaying
while (i < Number):
    if (i <= 1):
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
    i = i + 1