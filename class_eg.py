class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy","Golden Retriever", "Golden")
neighbours_dog = Dog("Tofu", "Poodle", 'Beige')
# Fetching the attributes of the class using objects
print(my_dog.breed)

print(my_dog.bark())

print(neighbours_dog.bark())
