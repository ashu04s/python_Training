list =[]
sum =0
n = int(input("enter size of the list"))
for i in range(1,n+1):
    item =int(input("enter list item"))
    
    list.append(item)
    
key = int(input("enter element you want to search"))
for i in list:
    if i==key:
        print(f"found at index {i}")
    else:
        pass       
    