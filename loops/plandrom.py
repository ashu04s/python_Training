num = int(input("enter a no"))
temp = num
rev =0
while(num>0):
    rem = num % 10
    rev = rev  *10 + rem
    num = num//10
if(temp == rev):
    print( f"{temp} is plandromie") 
else:
    print("not")       
    
    
    