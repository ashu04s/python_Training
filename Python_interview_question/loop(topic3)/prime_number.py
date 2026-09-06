a = int(input("Enter first value: "))
for i in range(2, a):
    if a % i == 0:
        print("not prime")
        break
    else:
        print("prime")