class Dog:

#class attribute
    species = 'mammal'

#initializer / instance attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age

#instance method

    def description(self):
        return "{} is {} years old ".format(self.name , self.age)

#instance method

    def speak(self,sound):
        return "{} says {}".format(self.name,sound)

#instantiate the Dog object

mikey = Dog("Mikey", 6)

#call our instance methods

print(mikey.description())
print(mikey.speak("Gruff Gruff"))

