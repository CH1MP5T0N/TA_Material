#These are how inputs are
start = input("Input number: ")
print(type(start))

#Eval works like this
start = eval(input("Input number: "))
print(type(start))

#You can make wacky stuff with input- like calculators
quick_maths = eval(input("Input number 1:"))
quick_maths2 = eval(input("Input number 2: "))
print(quick_maths + quick_maths2)

