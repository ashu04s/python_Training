l1 = [10, 20, 30, 40]
l2 = [20, 40, 50, 60]

common = []

for x in l1:
    if x in l2:
        common.append(x)

print("Common elements =", common)