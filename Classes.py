class Person:
    def __init__(self, firstname, lastname, health, status):
        """"initialize attributes to be used in/avaible for all / class method
        in this class, and for class objects created by this class."""
        #this below attribute is characteristic to the name self.
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
    def introduce(self):
        #All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname,self.lastname))

    def emote(self):
        emotion=random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now.".format(self.firstname))
    def status_change(self):
        if self.health == 100:
            print("{} is totally healtthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health <= 76:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <= 50:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format[self.firstname])

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "jones", 88, status=False)
Lee = Person("Lee","Williams", 72, status=True)
print("{} is my friend? {}".format(Maria.firstname,Maria.status))
print("{} is my friend? {}".format(Rey.firstname,Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()