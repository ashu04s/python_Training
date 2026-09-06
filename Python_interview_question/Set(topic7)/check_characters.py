s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = set(s1)
s2 = set(s2)

if s1.issubset(s2):
    print("All characters of first string are present")
else:
    print("All characters are not present")