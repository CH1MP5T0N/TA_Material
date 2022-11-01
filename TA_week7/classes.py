class Kenny:
    emir_noticed = True
    scrolling_vtuber = True
    classic_kenny_pose = True
    def __init__(self, emir):
        self.emir = emir

    def hey_emir(self):
        emir_noticed = True
        if emir_noticed == True:
            print("HEY", self.emir ,"LOOK AT THIS")    
    
kenny = Kenny("EMIR")
kenny.hey_emir()

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def __str__(self):
        return f"{self.name}{self.sound}"
dog = Animal("dog", "woof")     
print(dog)