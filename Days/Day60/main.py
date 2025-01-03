# getter, Setter in python

class MyClass:
    def __init__(self, value) -> None:
        self.value = value
    # @property
    def show(self):
        print(f"value is {self.value}")

    @property
    def tenXvalue(self):
        return 10 * self.value
    
    @tenXvalue.setter
    def tenXvalue(self, new_value):
        self.value = new_value

obj = MyClass(10)
obj.tenXvalue = 100
obj.show()
print(f"10XValue is {obj.tenXvalue}")
