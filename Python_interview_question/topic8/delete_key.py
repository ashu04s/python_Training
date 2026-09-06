d = {
    "name": "Ashu",
    "age": 20,
    "city": "Delhi"
}

key = input("Enter key to delete: ")

if key in d:
    del d[key]
    print("Dictionary =", d)
else:
    print("Key not found")