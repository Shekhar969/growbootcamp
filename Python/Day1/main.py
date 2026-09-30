s="shekhar"
print(s)

s="rawal"
age=24
role="QA"
print(s,age,role)


if s == "shekhar":
    print("Yes")
else:
    print("No")

#modulo at work 22/2 remender 0 => false 
if age%2:
    print("Odd Age")
else:
    print("Even Age")


#nested if statement
is_shekhar =False
if age >= 23:
    if is_shekhar:
        print("Heloooooo shekhar")
    else:
        print("where is shekhar")
else:
    print("Not old enough to be here")

loop=4
for i in range(2,loop):
    print(i)

items_loop=['shekhar','rawal','qa']
for il in range(len(items_loop)):
    print(items_loop[il])

print(items_loop[1])


while age < 25:
    age = age + 1
    print("helooaaaa")

t1 = 1
print(type(t1))

t1 = [1]
print(type(t1))

t1 = {1}
print(type(t1))

t1 = (1,)
print(type(t1))

 #functions 
a = 4
b = 5
def ADD(a, b):
    c = a + b
    print(a, "+", b, "=", c)

ADD(a,b)