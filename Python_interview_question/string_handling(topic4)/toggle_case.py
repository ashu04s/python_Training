s = input("Enter a string: ")

new = ""

for ch in s:
    if ch.isupper():
        new = new + ch.lower()
    elif ch.islower():
        new = new + ch.upper()
    else:
        new = new + ch

print("After toggle =", new)