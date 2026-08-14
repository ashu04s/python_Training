num = 20
i =0
even=0
odd=0
while(i<=num):
    if(i%2==0):
        even = even+1
    else:
        odd = odd+1
    i=i+1     
print(f"total even number up to 20 is {even}")        
print(f"total odd number up to 20 is {odd}")        
            