d = {
    "name": "Ashu",
    "age": 20,
    "city": "Delhi"
}

key = input("Enter key to search: ")

if key in d:
    print("Key exists")
else:
    print("Key does not exist")