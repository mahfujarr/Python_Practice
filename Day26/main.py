#Exercise: print something according to time
import time

t =int(time.strftime("%H"))
# t = int(input("Type a number: "))
print(t)

if (t >= 0 and t < 12):
    print("Good Morning")

elif (t >= 12 and t < 18):
    print("Good Afternoon")

elif (t >= 18 ):
    print("Good Night")