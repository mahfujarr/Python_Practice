# Map, Filter & Reduce

def cube(x):
    return x**3

l = [1,2,3,4,5,6]
# print(l)
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube, l))       #Map function
print(newl)

def filter_function(a):
    return a>3
newlf = list(filter(filter_function, l))    #filter function
newlf = list(map(cube, newlf))
print(newlf)

from functools import reduce

def mysum(x,y):
    return x + y

sum = reduce(mysum, l)
print(sum)