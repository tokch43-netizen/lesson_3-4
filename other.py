class dog:
    def __init__(self, age, weight, breed, height):
        self.age = age
        self.weight = weight
        self.breed = breed
        self.height = height

dog = dog(3, 12, "Husky", 50)

print("Age - ", dog.age)
print("Weight - ", dog.weight)
print("Breed - ", dog.breed)
print("Height - ", dog.height)