d = {
    "a": 10,
    "b": 50,
    "c": 30,
    "d": 20
}

key = max(d, key=d.get)

print("Key with maximum value =", key)
print("Maximum value =", d[key])