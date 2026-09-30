class MyName:
    name="shekhar"

stu1= MyName.name
print(stu1)

class Student:

    def __init__(self,name,rollno,marks):
        self.StudentName=name
        self.StudentRollNO=rollno
        self.StudentMarks=marks

    def showDetail(self):
        print("Student Name:", self.StudentName)
        print("Student Roll NO:", self.StudentRollNO)
        print("Student Marks:", self.StudentMarks)

    def interduce(self):
        print("I am ",self.StudentName, "And My roll number is", self.StudentRollNO )

student1= Student("shekhar",32,22)
student2= Student("rawal",22,12)

student2.showDetail()
student1.interduce()



