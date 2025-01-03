#Enumerate in python

marks = [12,56,14,78,98,72,14,63,87,24]

'''

i = 0
for m in marks:
    print(m)
    if (i == 4):                        (Without Enumerator)
        print("Congrats")
    i +=1

'''  

for i, m in enumerate(marks):
    print(m)
    if (i == 4):
        print("Congrats")
    elif(i == 8):
        print("Nice")
    