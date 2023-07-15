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
print(a.endswith("m"))
print(a.find("h"))
print(a.endswith("h",5,6))
print(a.find("hm"))
print(a.isalnum())
print(d.isalnum())
