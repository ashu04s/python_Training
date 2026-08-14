num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 =int(input("Enter the third number: "))
if(num1==num2):
    if(num1!=num3):
        print(num3,"is unique number")
elif(num1==num3):
    if(num1!=num2):
        print(num2,"is unique number")
elif(num2==num3):
    if(num2!=num1):
        print(num1,"is unique number")
else:
    print("no number is unique")    