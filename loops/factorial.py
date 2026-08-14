num = int(input("enter a no"))
fact = 1
if(num ==0):
    print(f"factorial of 0 is 1")
else:    
   while(num>1):
    fact = fact*num
    num =num-1

print(f"factorial of  is:{fact}")    