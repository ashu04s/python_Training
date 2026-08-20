n = 4
temp = n
dig = 0
final = 0   
while n > 0:
    rem = n % 10
    fact = 1
    while(rem > 0):
        fact = fact * rem
        rem = rem- 1
    final = final+ fact
    n = n//10
print(final)

if(temp  ==final):
    print("yes a strong number")
else:
    print("not a strong number")    