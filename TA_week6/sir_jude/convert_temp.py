def convert_temp():
    farenheit = eval(input("The temperature in Farenheit: "))
    celsius = 5/9 * (farenheit - 32)
    kelvin = celsius + 273.15
    print("The temperature in Celsius is: ", celsius)
    print("The temperature in Kelvin is: ", kelvin)
convert_temp()