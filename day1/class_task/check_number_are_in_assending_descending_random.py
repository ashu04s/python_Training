num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 =int(input("Enter the third number: "))
if(num1<num2 and num2<num3):
    print("Numbers are in ascending order")
elif(num1>num2 and num2>num3):
    print("Numbers are in descending order")
else:
    print("Numbers are in random order")