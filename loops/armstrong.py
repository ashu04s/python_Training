n = int(input("Enter a a number"))
temp = n
arm  = 0
length = len(str(n))
while(n>0):
    rev = n%10
    arm = arm + (rev**length)
    n= n//10
print(arm)
if(temp == arm):
    print("yes this armstrong")
else:
    print("no")    