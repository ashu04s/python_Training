try:
    n=int(input("enter a no"))
    
except ValueError:
    print("please enter integer type value")
    
result = 10/n
print(result)              