class Dog:



    species = 'mammal'


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def decription(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)



jun = Bulldog("Jun", 12)
print(jun.decription())



print(jun.run("slowly"))


print(isinstance(jun, Dog))


julie = Dog("Julie", 100)
print(isinstance(julie, Dog))


Johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(Johnnywalker, Bulldog))

                        #ตัวหลัง คือ Class
print(isinstance(julie, jun))