#Global and Local Varibales 

name="shekhar"
print(name)
def outter():
    print("outter fuction accessed")
    lastName="rawal"
#    print(age). // this will create an errror age is not defined

    def inner():
        print("Inner function called")
        print(lastName)
        age=22
        return lastName

    return inner()


print("Outside the function")

print(name)
lastNameReturnValue=outter()
print("lastNameReturnValue "+lastNameReturnValue)
