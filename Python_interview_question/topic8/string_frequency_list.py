l = ["apple", "banana", "apple", "mango", "banana", "apple"]

d = {}

for x in l:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

print(d)