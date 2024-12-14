class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Chirp!")

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("...")


def animal_sounds(animal):
    animal.speak()

dog = Dog("Whitey")
cat = Cat("Muning")
bird = Bird("Big Bird")
fish = Fish("Nemo")

animals = [dog, cat, bird, fish]

for animal in animals:
    animal_sounds(animal)