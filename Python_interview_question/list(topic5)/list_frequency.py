l = [10, 20, 10, 30, 20, 10]

new = []

for x in l:
    if x not in new:
        print(x, "=", l.count(x))
        new.append(x)