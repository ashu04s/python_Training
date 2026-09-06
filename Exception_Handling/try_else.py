try:
    n=int(input("enter a no"))
    result = 10/n

except ValueError:
    print("Invalid character")
    
except ZeroDivisionError:
    print("donot enter zero")

else:
    print("Success:", result)