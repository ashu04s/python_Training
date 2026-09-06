t = (10, 20, 30, 40, 50)

n = int(input("Enter item to remove: "))

l = list(t)

if n in l:
    l.remove(n)
    t = tuple(l)
    print("Tuple =", t)
else:
    print("Item not found")