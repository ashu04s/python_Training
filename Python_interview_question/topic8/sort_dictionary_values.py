d = {
    "a": 40,
    "b": 10,
    "c": 30,
    "d": 20
}

new = dict(sorted(d.items(), key=lambda x: x[1]))

print("Sorted by values =", new)