#Exercise: print something according to time
import time

t =int(time.strftime("%H"))
# t=19
n =input("Type your name: ")
# n="Mahfujar"
print(t)

if (t >= 18 ):
    print("Good Night,", n)

elif (t >= 12):
    print("Good Afternoon,", n)

elif (t >= 0):
    print("Good Morning,", n)