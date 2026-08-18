words = ["hello", "apple", "world"]

count = 0

for element in words:
    for j in element:
        if j in "aeiou ":
            count = count + 1

print(count)