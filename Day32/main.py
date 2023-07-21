#Sets in Python

s1 = {1,2,4,6,5,3}
s2 = {3,8,9,7,1,4,6}
print(s1.union(s2))                 #prints the union of both sets
print(s1.intersection(s2))          #prints the intersection of both sets

print(s1.issuperset(s2))            #boolean format

s1.update(s2)                       #adds item from s2 and updates the s1 set
# print(s1)

print(s1.issuperset(s2))            #boolean format

s1.add(10)                          #adds an element 10 to s1 set 
print(s1)                  \

s1.clear()                          #clears all elements in a set
print(s1)

if 1 in s1:
    print("yes")
else:
    print("No")
#Obviously It'll print no because "s1.clear()" cleared 
#all elements inside s1 so it's now empty

