l = [10, 20, 30, 40, 50]

n = int(input("Enter element to delete: "))

if n in l:
    l.remove(n)
    print("List =", l)
else:
    print("Element not found")