number1 = int(input("Enter the first number : "))  # Taking the input from the user for num1
number2 = int(input("Enter the second number : "))   # Taking the input from the user for num2

print("***Select operation***\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.FLOORDIV\n6.MOD\n7.SQR")
choice = input("Enter your choice : ")   # Taking the input from the user for which arithmetic operation to be performed

if choice == "1":   # If the choice is 1 it will do addition
    print("Your choice is ADD \n Output = ", number1 + number2)
elif choice == "2":   # If the choice is 2 it will do subtraction
    print("Your choice is SUB \n Output = ", number1 - number2)
elif choice == "3":   # If the choice is 3 it will do multiplication
    print("Your choice is MUL \n Output = ", number1 * number2)
elif choice == "4":   # If the choice is 4 it will do division
    print("Your choice is DIV \n Output = ", number1 / number2)
elif choice == "5":   # If the choice is 5 it will do floor division
    print("Your choice is FDIV \n Output = ", number1 // number2)
elif choice == "6":   # If the choice is 6 it will do Modulus
    print("Your choice is MOD \n Output = ", number1 % number2)
elif choice == "7":   # If the choice is 7 it will do square off number 1
    print("Your choice is SQR \n Output = ", number1 ** number2)
else:
    print("Not an valid input\nPlease try again!")   # if it is an invalid input this will throw an error



