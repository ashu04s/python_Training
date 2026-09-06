t = (10, 15, 20, 25, 30, 35)

new = []

for x in t:
    if x % 2 != 0:
        new.append(x)

t = tuple(new)

print("Odd values =", t)