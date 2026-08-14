num1 = int(input("Enter first no "))
num2 = int(input("Enter second no "))
symbol = input("please enter symbol like +,-,*,/,% ")
if symbol=="+":
    print(f"sum of {num1} and {num2} is {num1+num2}")
elif symbol=="-":
    print(f"subtraction of {num1} and {num2} is {num1-num2}")
elif symbol=="*":   
    print(f"multiplication of {num1} and {num2} is {num1*num2}")    
elif symbol=="/":
    print(f"division of {num1} and {num2} is {num1/num2}")
elif symbol=="%":
    print(f"modulus of {num1} and {num2} is {num1%num2}")   
else:
    print("Invalid symbol")