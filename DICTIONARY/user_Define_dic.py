n = int(input("enter how many item"))
dict ={}
for i in range(1,n+1):
    key = input("enter key  ")
    value =input(f"enter the value of {key}")
    dict[key] =value
    
    
print(dict)    