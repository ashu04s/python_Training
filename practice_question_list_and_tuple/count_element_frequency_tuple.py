numbers = (1, 2, 3, 2, 4, 2, 5)

element = int(input("Enter element: "))

count = 0

for i in numbers:
    if i == element:
        count += 1

print("Freq:", count)