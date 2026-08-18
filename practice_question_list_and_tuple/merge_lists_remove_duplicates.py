list =[1,2,3,4,5]
list2 =[1,6,4,3,8]
new = list+list2
for i in new:
    if i in new:
        new.remove(i)
        
print(new)        