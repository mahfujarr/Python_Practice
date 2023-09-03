# Instance Vs. Class variables

class Employee:
    companyName = "Apple"               #Class variable
    def __init__(self, name) -> None:
        self.name = name                #instance variable
        self.raise_amount = 2           #instance variable
    
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Mahfujar")
# emp1.showDetails()
Employee.showDetails(emp1)
