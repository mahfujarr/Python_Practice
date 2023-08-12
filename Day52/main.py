# Lambda functions in python

#instead of doing 
# def math(x):
#     return x**2
#I can do it with Lambda function like this:
def ap(fx, value):
    return 10 + fx(value)

math = lambda x: x**2
avg = lambda x, y, z: (x+y+z)/3


print(f"The square is : {math(5)}")

print(f"The average is : {avg(3,5,10)}")

print(ap(math, 2))      #Used math as a function of 2  
print(ap(lambda x:x**3, 3))     #Used "lambda x:x**3" as a function of 2