n = int(input("Enter a three digit number: "))
sum =0
while n>0:
    rev = n%10
    sum = sum + rev
    n = n//10



print("Sum of digits =", sum)