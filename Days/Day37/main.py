#finally keyword in python
def func1():
        try:
                l = [1,3,2,4,5]
                i = int(input("Enter the index: "))
                print(l[i])
                
        except:
                print("Invalid index")
        finally:
                print("I am always executed")
                return 0
x = func1()
print(x)