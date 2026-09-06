s = input("Enter a sentence: ")

words = s.split()

long = words[0]

for word in words:
    if len(word) > len(long):
        long = word

print("Long =", long)