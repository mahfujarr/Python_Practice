# static method in python

class Math:
    def __init__(self, num) -> None:
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n
    

    @staticmethod
    def add(a,b):          #No need of "self"
        return a + b
    
a = Math(5)
print(a.num)
a.addtonum(1)
print(a.num)
print(a.add(5,5))