list = [1,2,3,4,5,89,423,43,23]
even =[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
        
print(f"even list {even}")        
print(f"odd list {odd}")        
        