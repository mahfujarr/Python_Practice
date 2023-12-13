# strings are immutable

a="!!!Mahfujar!!!!!!!!!!!!!!"

b="1 0 1 5 2 5"

c="joy is a Loser"

d="Mahfujar"

print(len(a))
print(a.upper())
print(a.lower())
print(a.lstrip('!'))
print(a.rstrip("!"))
print(a.replace("Mahfujar","Joy"))
print(b.split(' '))
print(c.capitalize()) #It's "casefold" if I want to print in small letter!
print(c.casefold())
print(a.center(50))
print(len(a.center(50)))
print(a.count("M")) #case sensitive
print(a.endswith("!"))
print(d.endswith("!"))
print(a.find("h"))
print(a.endswith("h",5,6))
print(a.find("hm")) 
'''The find() method,
    1)finds the first occurrence of the specified value
    2)returns -1 if the value is not found.
    3)almost the same as the index() method,
    the only difference is that the index() method raises an exception
    if the value is not found.'''
print(a.isalnum())
print(d.isalnum())