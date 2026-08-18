list =[1,23,4,343,23,4,324,-21,12,-12]
even =0
odd=0
postive=0
negative=0
for i in list:
    if i%2==0:
        even =even+1
    else:
        odd=odd+1
            
for i in list:
    if i>0:
        postive=postive+1
    else:
        negative=negative+1            
                    
print(even)        
print(odd)        
print(negative)        
print(postive)        