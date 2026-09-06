a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping:")
print(f"a = {a}, b = {b}")
a = a+b
b = a-b
a = a-b
print("After swapping:")
print(f"a = {a}, b = {b}")