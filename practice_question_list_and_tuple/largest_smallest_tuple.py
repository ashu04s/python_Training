numbers = (10, 5, 25, 3, 18)

largest = 0
smallest = 999

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)