#Constructors in Python

class person:
    def __init__(self, n, a):
        # n = self.name     #Not this
        # a = self.age      #Not this
        self.name = n       #Use like this
        self.age = a        #Use like this
    def info(self):
        print(f"Age of {self.name} is {self.age}")

a = person("Mahfujar", 20)
a.info()

b = person("Mahrufur", 16)
b.info()