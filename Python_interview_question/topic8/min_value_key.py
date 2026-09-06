d = {
    "a": 10,
    "b": 50,
    "c": 30,
    "d": 20
}

key = min(d, key=d.get)

print("Key with minimum value =", key)
print("Minimum value =", d[key])