n = int(input("enter the size of the dic"))
dict ={}
for i in range(1,n+1):
    key = (input("enter key"))
    value =input("ennter the value")
    dict[key] =value
    
for i  in dict:
    print(f"the key is {i} and value {dict[i]}")       