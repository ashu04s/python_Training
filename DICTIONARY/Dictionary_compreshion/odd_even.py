numbers = range(1, 6)

result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}
print(result)