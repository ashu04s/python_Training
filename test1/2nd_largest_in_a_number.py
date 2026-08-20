n = int(input("Enter a numbe"))
max =0
second_max=0
while n>0:
    digit = n % 10
    if digit>max:
        max =digit
    elif digit>second_max and digit<max:
        second_max =digit
    else:
        pass    
    n = n//10   
print(second_max)       
