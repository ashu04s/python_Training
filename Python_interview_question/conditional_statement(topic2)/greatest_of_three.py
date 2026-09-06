a = int(input("Enter first value: "))
b = int(input("enter second value"))
c = int(input("enter third value"))

if a>b and a>c:
    print(f"{a} is the largest")
elif b>a and b>c:
    print(f"{b} is the largest")    
else:
    print(f"{c} is the largest")