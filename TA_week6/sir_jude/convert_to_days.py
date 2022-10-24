def convert_to_days():
    hours = eval(input("Enter number of hours: "))
    minutes = eval(input("Enter number of minutes: "))
    seconds = eval(input("Enter number of seconds: "))
    return hours, minutes, seconds


def getdays(hours, minutes, seconds): 
    hours = hours * 3600
    minutes = minutes * 60
    seconds = seconds + minutes + hours
    seconds = seconds / 86400
    print(round(seconds, 4))
    
hours, minutes, seconds = convert_to_days()
getdays(hours, minutes, seconds)

