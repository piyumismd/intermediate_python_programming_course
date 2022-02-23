class Dog:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.energy = 5

    def describe(self):
        return f"{self.name} is {self.colour}"

    def stamina(self):
        print(f"{self.name} have {self.energy} number of energy")
        print(f"{self.name} is {self.colour} and have {self.energy} number of energy")

    def reduce_stamina(self):
        while self.energy:
            self.energy -= 1
            print(f"{self.name}'s energy is now: {self.energy}")
        print(f"{self.name} have {self.energy} energy and he is hungry now")


our_dog = Dog("Bruno", "brown")
other_dog = Dog("Shaggy", "black")
good_dog = Dog("Pudding", "white")

print(our_dog.describe())
print(good_dog.describe())
print(other_dog.describe())
other_dog.stamina()
other_dog.reduce_stamina()
