s = input("Enter a string: ")

max_ch = ""
max_count = 0

for ch in s:
    count = s.count(ch) # count the frequency of character ch in string s

    if count > max_count:
        max_count = count
        max_ch = ch

print("Maximum frequency character =", max_ch)
print("Frequency =", max_count)