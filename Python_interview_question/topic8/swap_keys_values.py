d = {
    "a": 10,
    "b": 20,
    "c": 30
}

new = {}

for key, value in d.items():
    new[value] = key

print("Swapped dictionary =", new)