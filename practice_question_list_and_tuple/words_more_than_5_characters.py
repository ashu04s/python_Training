words = ["apple", "banana", "cat", "elephant", "school"]

new = []

for i in words:
    if len(i) > 5:
        new.append(i)

print(new)