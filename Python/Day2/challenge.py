print("1")

def outer():
    print("2")

    def inner():
        print("3")
        return "X"

    print("4")
    return inner

print("5")

func = outer()

print("6")

value = func()

print("7")
print(value)

# 1 5 2 4 6 3 7 x