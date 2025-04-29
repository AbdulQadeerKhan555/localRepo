# PYTHON MATCH CASE STATEMENT
x = int(input("Enter the value of x   "))
match x:
    case 1:
        print("The value of x is 1")
    case 4:
        print("The value of x is 4")
    case _:
        print("The value of x is not 1 or 4")
   