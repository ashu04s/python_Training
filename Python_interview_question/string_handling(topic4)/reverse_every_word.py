s = input("Enter a sentence: ")

words = s.split()

print(words)

for word in words:
    print(word[::-1], end=" ")
    print(type(word))