#one design pattern
r =5
c =5
for i in range(1,r+1):
    for j in range(1,c+1):
        if(j==3 or i==5 or (i==2 and j==2) ):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")    
    print()        