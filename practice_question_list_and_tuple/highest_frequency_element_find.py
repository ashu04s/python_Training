list =[1,2,3,2,3,5,2,34,2,32,1,3,34,2,3,2,2,2]
max_freq =0
for i in list:
    a = list.count(i)
    if a>max_freq:
        element=i
        max_freq=a
    else:
        pass
print(f"{element} has frequency which is {max_freq}")         