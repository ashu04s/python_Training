s = input("Enter a string: ")

v = set()

for ch in s:
    if ch in "aeiouAEIOU":
        v.add(ch.lower())

print("Vowels =", v)