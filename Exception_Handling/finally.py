# finally also execute if Exception come or not

try: 
    n =int(input("enter a no"))
    result = 10/n
except ZeroDivisionError:
    print("donot enter zero")
    
finally:
    print("Always execute")
                