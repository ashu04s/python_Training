num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if(num1==num2):
    if(num1!=num3):
        print(num1,"and",num2,"are equal")
elif(num1==num3):
    if(num1!=num2):
        print(num1,"and",num3,"are equal") 
elif(num2==num3):
    if(num2!=num1):
        print(num2,"and",num3,"are equal")  
else:
    print("no two numbers are equal")                       
       