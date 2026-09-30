print("outside all the class")

class students():

    course="BscCsit" # Public
    _feepermonth=2000 # Protected
    __studentpass=1234 # Privite

    def showpassword(self):
         print("Your password is ", self.__studentpass)

class student(students):

        def __init__(self,name):
             self.name=name

#        studentpass=students.__studentpass

        def intro(self):
          print("Hello", self.name, "Your Selected course is", students.course,"Your fee per sem is",students._feepermonth*6 )

std=student("shekhar")

std.intro()
std.showpassword()