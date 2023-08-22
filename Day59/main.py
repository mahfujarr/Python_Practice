#Python Decorator

def greet(fx):
    def mfx(*args, **kwargs):       #*args takes arguments as a Tuple
        print("Good Morning,")      #*kwargs takes arguments as a Dict
        fx(*args, **kwargs)
        print("This is great function.")
    return mfx

@greet
def hello():
    print("Mahfujar Rahman.")
                            #Or,
# greet(hello)
hello()

@greet
def add(a, b):
    print(a + b)

add(1,1)
