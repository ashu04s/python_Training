words = ["apple", "ant", "ball", "bat", "cat"]

d = {}

for word in words:
    ch = word[0]

    if ch not in d:
        d[ch] = []

    d[ch].append(word)

print(d)