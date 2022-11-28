#Inheritance
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def printname(self):
        print(self.first, self.last)
    def talk(self):
        print("HI IM A PERSON")

var = Person("James", "Baxter")
var.talk()

class Student(Person):
    def __init__(self, first, last):
        Person.__init__(self, first, last)
    def introduction(self):
        print("Hello my name is", self.first, self.last)

var2 = Student("Big", "Chode")
var2.talk()

#Exercise 1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def display(self):
        print("Vehicle name:", self.name, "Speed:", self.max_speed,"Mileage", self.mileage)
bus = Bus("School Volvo", 180, 12)
bus.display()