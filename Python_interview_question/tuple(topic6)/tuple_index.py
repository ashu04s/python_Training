t = (10, 20, 30, 40, 50)

n = int(input("Enter value: "))

if n in t:
    print("Index =", t.index(n))
else:
    print("Value not found")