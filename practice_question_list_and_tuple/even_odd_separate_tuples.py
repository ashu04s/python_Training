numbers = (1, 2, 3, 4, 5, 6, 7, 8)

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even = tuple(even)
odd = tuple(odd)

print("Even:", even)
print("Odd:", odd)
