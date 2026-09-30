try:
    x=int(23)
    y=int(56)
    name=str("Shekhar")

except ValueError:
    print("Enter the correct values")

else:
    print("Two values are",x,y,"and Name is ",name)

finally:
    print("successfully run the code")