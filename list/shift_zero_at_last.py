#shift zero at last
list =[1,2,3,4,0,7,0,4,0,6]
for i in list:
    if i==0:
        list.append(i)
        list.remove(i)
    else:
        pass     
print(list)



  