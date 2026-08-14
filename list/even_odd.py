

even =[]
odd =[]
n = int(input("enter range of list "))
for i in range(1,n+1):
    item = int(input(f"enter item {i} "))
    if(item%2==0):
        even.append(item)
    else:
        odd.append(item)   
print(list) 
print(even)
print(odd)