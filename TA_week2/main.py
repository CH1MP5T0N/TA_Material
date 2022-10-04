# IF STATEMENTS
while True:
    choice = eval(input("Enter a number: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n"))
    if choice == 1:
        number1 = eval(input("Enter number1: "))
        number2 = eval(input("Enter number2: "))
        print(number1 + number2)
    elif choice == 2:
        number1 = eval(input("Enter number1: "))
        number2 = eval(input("Enter number2: "))
        print(number1 - number2)
    elif choice == 3:
        number1 = eval(input("Enter number1: "))
        number2 = eval(input("Enter number2: "))
        print(number1 * number2)
    elif choice == 4:
        number1 = eval(input("Enter number1: "))
        number2 = eval(input("Enter number2: "))
        print(number1 / number2)
    else:
        print("INVALID INPUT")

# x = 200
# y = 30
# z = 500

# if x > y or z > y:
#     print("yipee")