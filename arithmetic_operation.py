"""The code is regarding the arithmetic operations in python

This code is for calculating 2 input numbers from the user and choosing the arithmetic operation."""

number1 = int(input("Enter the first number : "))  
number2 = int(input("Enter the second number : "))   

print("***Select operation***\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.FLOORDIV\n6.MOD\n7.SQR")
choice = input("Enter your choice : ")  

if choice == "1": 
    print("Your choice is ADD \n Output = ", number1 + number2)
elif choice == "2": 
    print("Your choice is SUB \n Output = ", number1 - number2)
elif choice == "3":   
    print("Your choice is MUL \n Output = ", number1 * number2)
elif choice == "4":   
    print("Your choice is DIV \n Output = ", number1 / number2)
elif choice == "5":   
    print("Your choice is FDIV \n Output = ", number1 // number2)
elif choice == "6": 
    print("Your choice is MOD \n Output = ", number1 % number2)
elif choice == "7":  
    print("Your choice is SQR \n Output = ", number1 ** number2)
else:
    print("Not an valid input\nPlease try again!")  



