s = input("Enter a string: ")

a = 0
d = 0
sp = 0

for ch in s:
    if ch.isalpha():
        a = a + 1
    elif ch.isdigit():
        d = d + 1
    else:
        sp = sp + 1

print("Alphabets =", a)
print("Digits =", d)
print("Special =", sp)