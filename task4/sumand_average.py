list =[]
sum =0
n = int(input("enter size of the list"))
for i in range(1,n+1):
    item =int(input("enter list item"))
    list.append(item)
    sum = sum+item

average = sum/n    
    
print(f"orginail list {list}") 
print(f"sum of the list {sum}")   
print(f"average of the list {average}")   