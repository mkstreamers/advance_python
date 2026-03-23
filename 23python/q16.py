#16. Design a School Management System that includes classes for Student, Teacher, and Admin, each with unique behaviors.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student:", self.name, "Marks:", self.marks)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print("Teacher:", self.name, "Subject:", self.subject)


class Admin:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Admin:", self.name)


s = Student("Alice", 85)
t = Teacher("Mr. Smith", "Math")
a = Admin("Principal")

s.display()
t.display()
a.display()