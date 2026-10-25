class Dog:
    animal = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

dog1 = Dog("Bulldog", "Brown")
dog2 = Dog("Labrador", "Black")

print("dog1.animal, dog1.breed, dog1.color")
print("dog2.animal, dog2.breed, dog2.color")