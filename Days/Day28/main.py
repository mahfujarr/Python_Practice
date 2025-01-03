#f-strings in python

string = "My name is {} & I live in {}."
name = "Mahfujar"
place = "Sundarganj"
print(string.format(name, place))
print(f"My name is {name} & I am from {place}.") #f-string

# price = 69.999

txt = "For only $ {price:.2f}!" #{price:.2f} prints only 2 decimal places.
print(txt.format(price = 69.999))


print(f"{2 * 30}")