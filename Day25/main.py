#Operations on Tuples

tup1=(1,2,5,4,6,3,2,4,1,3,2,1,5,6,4)
ans1 = tup1.count(2)        #counts how many times 2 has been repeated inside tuple
print(ans1)                  #prints the ans1

ans2 = tup1.index(4)       #prints the index of the first ocurrence of specified value
print(ans2)

ans3 = tup1.index(5, 5, 14)
print(ans3)

ans4 = len(tup1)
print(ans4)

