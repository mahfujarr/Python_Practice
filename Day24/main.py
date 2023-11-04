#Tuple in Python

tup = (3,4,1,6,2,5, "Mahfujar", False)
print(type(tup))
print(len(tup))
print(tup[0], (tup[1]), (tup[2]), (tup[3]), (tup[4]), (tup[5]), (tup[6]), (tup[7]))

if "Mahfujar" in tup:
    print("Present")
else:
    print("Not found")

tup2 = tup[1:5]
print(tup2)