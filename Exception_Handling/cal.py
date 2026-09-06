


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    
    print(add)
    print(mul)
    print(sub)
    print(div) 
    

except (ValueError, ZeroDivisionError):
    print("Please not enter sring or  zero.")
 
      