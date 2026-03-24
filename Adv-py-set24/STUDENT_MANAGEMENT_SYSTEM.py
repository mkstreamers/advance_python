#20. Build mini project:
#STUDENT MANAGEMENT SYSTEM
#Features:
#- Add student
#- View student
#- Delete student
#- Store data in file or database
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print(f"Student {name} added successfully.")
    
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
    
    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted successfully.")
                return
        print(f"Student {name} not found.")
sms = StudentManagementSystem()
sms.add_student("Alice", 20, "A")
sms.add_student("Bob", 22, "B")
sms.view_students()
sms.delete_student("Alice")
sms.view_students()
#OUTPUT: Student Alice added successfully.
#        Student Bob added successfully.    
#        Name: Alice, Age: 20, Grade: A
#        Name: Bob, Age: 22, Grade: B
#        Student Alice deleted successfully.
#        Name: Bob, Age: 22, Grade: B   

