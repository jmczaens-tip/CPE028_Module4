class Student:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"{self.name}({self.age})({self.gender})"

p1 = Student("Jose Mari Zaens", 23, "Male")
print(p1)
p2 = Student("Nerrad P", 20, "Female")
print(p2)
print("Name:", p1.name)
print("Name:", p1.age)
print("Name:", p1.gender)

print("Name:", p2.name)
print("Name:", p2.age)
print("Name:", p2.gender)