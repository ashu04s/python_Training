# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print(k+1,end=" ")
#     print()

n=1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()    