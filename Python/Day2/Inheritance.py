class normalUser():
    def edit(self):
        print("Edit is performed")

class Admin(normalUser):
    def changepass(self):
        print("password is change")

shekhar=Admin()

shekhar.edit()
shekhar.changepass()