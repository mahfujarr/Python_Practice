#Python Class & Objects


class person:
    name = "Mahfujar"
    age = 21
    gender = "Male"
    def info(self):
        print(f"Age of {self.name} is {self.age} & Gender is {self.gender}")


a = person()
b = person()
b.name = "Mahrufur"
b.age = 16
a.info()
b.info()