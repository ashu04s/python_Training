tuple1 = (1, 2, 3, 4, 2)
tuple2 = (2, 4, 5, 6, 2)

new = []

for i in tuple1:
    if i in tuple2 and i not in new:
        new.append(i)

new = tuple(new)

print(new)