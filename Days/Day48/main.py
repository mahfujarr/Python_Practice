# Local & global Variables

x = 10 #Global variable
print(x)


def var():
    y = 5 #Local variable
    global x
    x = 20
    print(y)

print(x)
var()
print(x) #here global variable is changed.