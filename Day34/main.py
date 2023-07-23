#Dictionary methods in Python

ep1 = {122: 45, 123: 89, 651:81, 213:56}

ep2 = {222:79, 234:46}

ep1.update(ep2)
print(ep1)

# ep1.clear()
# print(ep1)

ep1.pop(122)        #deletes the item "122"
print(ep1)

