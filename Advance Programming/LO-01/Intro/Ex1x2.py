class Dog:

    #Class Attribute
    species = 'mammal'

    # Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def description(self):
        return "{} is {} year old".format(self.name, self.age)

    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#Object
mikey = Dog("Mikey", 6)


print(mikey.description())
print(mikey.speak("Gruff Gruff"))