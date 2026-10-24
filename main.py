class Student:
    def __init__(self, name, age, height, number):
        self.name = name
        self.age = age
        self.height = height
        self.number = number

    def grow(self, height = 1):
        self.height += height


anton = Student("Anton", 12, 166, 19405495940)

print("Name - ", anton.name)
print("Age - ", anton.age)
print("Height - ", anton.height)
print("Phone number - ", anton.number)

anton.grow(height=5)
print(anton.height)