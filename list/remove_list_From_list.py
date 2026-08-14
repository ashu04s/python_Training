# remove list from list
list =[1,2,3,4,5,[],[],4 ]
list2 =[]
for i in list:
    if i == []:
       pass
    else:
        list2.append(i)