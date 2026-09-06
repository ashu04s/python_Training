l = [10, 20, 10, 30, 20, 40]

new = []

for x in l:
    if x not in new:
        new.append(x)

print("List after removing duplicates =", new)