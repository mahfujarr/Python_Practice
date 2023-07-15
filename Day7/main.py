# A simple calculator

n = int(input("Enter the first number: "))

m = int(input("Enter the second number: "))

ans1 = n+m
ans2 = n-m
ans3 = n*m
ans4 = n/m
ans5 = n%m
ans6 = n//m

print("Addition of",n,"and",m,"is", ans1)
print("Substraction of",n,"and",m,"is", ans2)
print("Multiplication of",n,"and",m,"is", ans3)
print("Division of",n,"and",m,"is", ans4)
print("Modulus of",n,"and",m,"is", ans5)
print("Floor Division of",n,"and",m,"is", ans6)