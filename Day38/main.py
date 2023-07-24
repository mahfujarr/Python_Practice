#Raising custom errors
a = input("enter a number between 5 & 9: ")

if(a == "quit"):
    print("you chose to quit")
elif (int(a) < 5 or int(a) > 9 ):
    raise ValueError("Value should be between 5 & 9")
