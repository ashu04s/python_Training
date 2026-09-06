try:

    number = int(input("Enter number: "))

    result = 10 / number

except ZeroDivisionError:

    print("Cannot divide by zero.")

print(result)