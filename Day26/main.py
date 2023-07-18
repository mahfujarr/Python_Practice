#Exercise: print something according to time
import time

t =int(time.strftime("%H"))
n =input("Type your name: ")
print(t)

if (t >= 0 and t < 12):
    print("Good Morning,", n)

elif (t >= 12 and t < 18):
    print("Good Afternoon,", n)

elif (t >= 18 ):
    print("Good Night,", n)
