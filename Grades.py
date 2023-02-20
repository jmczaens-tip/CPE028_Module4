class Grades:#Jose Mari C. Zaens
    def __init__(gr,Course_Code,Course_Unit,Course_Grade):
        gr.Course_Code = Course_Code
        gr.Course_Unit = Course_Unit
        gr.Course_Grade = Course_Grade
    def __str__(gr):
        return f"{gr.Course_Code}({gr.Course_Unit})({gr.Course_Grade})"

grades1 = Grades("CPE028","3 units","4th Year")
print(grades1)
