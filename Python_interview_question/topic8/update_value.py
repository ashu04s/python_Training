d = {
    "name": "Ashu",
    "age": 20,
    "city": "Delhi"
}

key = input("Enter key: ")
value = input("Enter new value: ")

if key in d:
    d[key] = value
    print("Dictionary =", d)
else:
    print("Key not found")