#List Methods

l=[2,5,4,3,1]
print(l)

l.append(6) #adds 6 on the list
print(l)

l.sort() #sorts the list by ascending order
print(l)

l.sort(reverse=True) #sorts the list in descending order
print(l)

l.reverse() #reverses the list
print(l)


print(l.index(4))  #returns the index of the first occurence of the item

print(l.count(5))  #counts how many times the number has been repeated on the list

m=l.copy()          #copies the list
m[0]= "Mahfujar"    #changes the first item of the list to "Mahfujar"
print(m)            #Finally prints the modified list

m.insert(1,1)       #inserts "1" to the second element of the modified list "m"
print(m)

l.extend(m)         #extends the list "l" at the end with the modified list "m" 
print(l)


k=l + m             #this will not modify the lists but will just add them together
print(k)