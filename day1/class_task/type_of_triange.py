a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
if(a==b and b==c and a==c):
    print("The triangle is equilateral")
elif(a==b or b==c or a==c):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")    