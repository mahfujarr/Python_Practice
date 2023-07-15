# if else conditions
import time
a=int(time.strftime('%H'))
# a=time.strftime('%H')
# a=int(input("Enter your age:\n"))
if (a < 12):
    print("Good Morning")
elif(a<18):
    print("Good Afternoon")
else:
    print("Good Night")
