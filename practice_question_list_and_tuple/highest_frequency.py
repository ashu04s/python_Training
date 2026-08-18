list = [1, 2, 3, 3,3,2 ,1, 2, 5]
new_list=[]
max_freq=0
for i in list:
    freq = list.count(i)
    if(freq>max_freq):
        max_freq=freq
    elif freq==max_freq and i not in new_list:
        new_list.append(i)
    else:
        pass       
          
print(new_list)