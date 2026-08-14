n = int(input("enter a no"))
if n==1 or n==0:
    print("number is not prime")
else:
    for i in range(2,n):
            if n%i==0:
                print(f"{n} is not prime no")
                break
            
    #  ya wala else for ka ha       
    else:
            print("number is a prime no")       