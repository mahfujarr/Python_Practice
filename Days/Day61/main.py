# Inheritance in Python
class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f' {self.id} is {self.name}\'s ID')

class Programmer(Employee): #Inherited contents from Employee Class
    def showLanguage(set):
        print("The default language is Python")

e1 = Employee("Rohan Das", 32)
e2 = Programmer("Mahfujar Rahman", 43)

e1.showDetails()
e2.showDetails()
e2.showLanguage()