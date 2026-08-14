num = int(input("Enter a no := "))
sum =0
for i in range(1,num):
    if(num%i==0):
        sum = sum+i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")            
    
    
# a number is said to be perfect number if     eska diviors ka sum us number
# ka sum ka barabar ho 