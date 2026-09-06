n = int(input("Enter a number: "))

temp = n
sum = 0
count = len(str(n))

while n > 0:
    a = n % 10
    sum = sum + a ** count
    n = n // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")