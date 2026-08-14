#two design pattern
r =5
c =5
for i in range(1,r+1):
    for j in range(1,c+1):
        if(  i==1 or i==3 or i==5 or (i==2 and j==5) or(i==4 and j==1) ):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")    
    print()        