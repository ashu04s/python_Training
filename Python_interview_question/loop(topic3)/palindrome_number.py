a = int(input("Enter first value: "))
temp =a
sum = 0
while a>0:
    rev = a%10
    sum = sum*10 + rev
    a = a//10

if(sum==temp):
    print("yes")
else:
    print("no   ")        
    