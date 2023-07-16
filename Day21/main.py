#function arguments

def averageof2(a = 1, b = 2):
    print("the average is: ", (a+b)/2)
    
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

averageof2()

name("Mahfujar", "Rahman", "Joy")

#tuple
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average of these", len(numbers), "numbers are: ", (sum / len(numbers)))

average(3,6,4)

#Dictionary
def dictName(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

dictName(mname="Rahman", lname="Joy",  fname="Mahfujar")


#return function
def number(*number):
    sum=0
    for i in number:
        sum = sum + i
    return sum / len(number)

c=number(1,2,3,4,5)
print("The average of these", len(number), "numbers are: ", c) #why This one gives an error???🤔