str1 ="ashu kumar verma"
l1 =str.split(str1)

print(l1)

for i in range(len(l1)-1):
    a =l1[i][0].upper()+"."
    print(a,end="")
    

print(l1[-1].title(),end="")    