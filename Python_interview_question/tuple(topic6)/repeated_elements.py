t = (10, 20, 10, 30, 20, 40, 10)

new = []

for x in t:
    if t.count(x) > 1 and x not in new:
        new.append(x)

print("Repeated elements =", new)