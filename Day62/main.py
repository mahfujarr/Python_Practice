# Access Modifiers in Python

# Public Access Modifiers
class Employee:
    def __init__(self) -> None:
        self.name = "Mahfujar Rahman"

a = Employee()
print(a.name)


# Private Access Modifiers
class Employee:
    def __init__(self) -> None:
        self.__name = "Mahfujar Rahman" #double underscore = private

a = Employee()
# print(a.__name) #Can not access directly
print(a._Employee__name) #name mangling   #Can be accessed indirectly
