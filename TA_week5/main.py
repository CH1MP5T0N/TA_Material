def factorial(n):
    if n == 1: #base case
        return n
    else:
        return n * factorial(n - 1) #recursive case

def iterative_factorial(n):
    i = 1
    for num in range(2, n + 1):
        i*= num
    return i
number = 10
print(number, "!= ", iterative_factorial(number))