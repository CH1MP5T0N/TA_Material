#dictionary of animals in a zoo and their respective weights
animals = {"Elephant": 250, "Lion": 89, "Penguin" : 25, "Crocodile": 97}
print(animals["Elephant"])
#Creating dictionary with dict()
mydict = dict(elephant = 250, lion = 89, penguin = 25, crocodile = 97)
#Adding a new element in the dictionary
mydict["Tortoise"] = 500
#Ways to remove elements from the dictionary
del mydict["penguin"]
print(mydict)
mydict.pop("crocodile")
print(mydict)
#Copying another dictionary
yourdict = mydict.copy()
#Looping through dictionary values
num = 0
for i in mydict.values():
    num += i
print(num)
#Looping through dictionary keys
for i in mydict:
    print(i)