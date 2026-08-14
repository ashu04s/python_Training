# hollow square pattern
# n = 5  
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print() 
    
    
r =5
c= 5
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==5 or j==5 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()           