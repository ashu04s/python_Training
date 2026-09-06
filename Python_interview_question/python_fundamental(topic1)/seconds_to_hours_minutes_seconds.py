sec = int(input("Enter total seconds: "))

hour = sec // 3600
sec = sec % 3600

min = sec // 60
sec = sec % 60

print("Hours =", hour)
print("Minutes =", min)
print("Seconds =", sec)