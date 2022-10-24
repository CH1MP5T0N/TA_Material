def calc_new_height():
    width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    desired_width = eval(input("Enter the desired width: "))
    formula = (desired_width * height) / width
    print(formula)
calc_new_height()