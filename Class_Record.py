import Student
import Grades

p1=Student.Student("Jose Mari C. Zaens", 24, "Male")
p1_grade = Grades.Grades("CPE028", "3 units", "Uno")
print(p1)
print(p1_grade)
print("Name:",p1.name)
print("Age:",p1.age)
print("Gender:",p1.gender)
print("Course Code:", p1_grade.Course_Code)
print("Course Unit:", p1_grade.Course_Unit)
print("Course Grade:", p1_grade.Course_Grade)