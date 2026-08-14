n = int(input("enter a no"))
sum = 0
rev =0
while n>0:
    rem=n%10
    sum = sum +rem
    n =n//10
print(sum)    