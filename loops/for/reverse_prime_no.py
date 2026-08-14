num = int(input("enter a no"))
num2 = num
sum = 0
reverse =1
reverse_prime =1
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime number")
        reverse =2
        break  
    else:
        print(f"{num} is a prime number ")
        break

while(num>0):
    rem = num%10
    sum = sum*10 + rem
    num = num//10
    
for i in range(2,sum):
    if sum%i==0:
        print(f"{sum} is not a prime number")
        reverse_prime =3
        break   
else:
    print(f"{sum} is a prime number")


if reverse == reverse_prime:
    print("this is reverse prime 🤗🤗🤗")
else:
    print("this is not reverse prime 😞😞😞")    
    