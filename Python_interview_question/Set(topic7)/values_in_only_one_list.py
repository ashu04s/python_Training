l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

s1 = set(l1)
s2 = set(l2)

s = s1.symmetric_difference(s2)

print("Values in only one list =", s)