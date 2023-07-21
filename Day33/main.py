#Dictionary in Python

dict = {
    "mahfujar"  : "Human",
    "spoon"     : "Object",
    "apple"     : "Food"
}
print(dict["mahfujar"])
print(dict["apple"])

info = {

    'name'  : 'Mahfujar',
    'gender': "Male",
    'eligible': 'no'
        
        }
# print(info.get('name'))
# print(info.get('age'))      #Won't throw an error 
# print(info["gender"])
# print(info["age"])          #will throw an error  because age wasn't defined

print(info.keys())

for key in info.keys():
    print(info[key])


for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

