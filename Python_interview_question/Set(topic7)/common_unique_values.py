l1 = [10, 20, 20, 30, 40]
l2 = [20, 30, 30, 50]

s1 = set(l1)
s2 = set(l2)

common = s1.intersection(s2)

print("Common unique values =", common)