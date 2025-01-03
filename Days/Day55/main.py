#snake water gun game
import random

def check(com, user):
    if com == user:
        return 0
    if(com == 0 and user == 1):
        return -1
    if(com == 1 and user == 2):
        return -1
    if(com == 2 and user == 0):
        return -1
    return 1
com = random.randint(0,2)
user = int(input("Enter 0 for snake\n1 for water\n2 for gun\n"))

print("You chose: ", user)
print("Computer chose: ", com)

score = check(com, user)
if(score == 0):
    print("It's a draw")
elif score == 1:
    print("You Lose")
else:
    print("You won")
