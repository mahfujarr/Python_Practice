#Recursion in Python

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

factorial(5)

# Function to create a fibonacci sequence

def fibonacci(n):
    if (n==0 or n==1):
        return 1
    else:
        return (fibonacci(n-1))+(fibonacci(n-2))
    
fibonacci(8)
