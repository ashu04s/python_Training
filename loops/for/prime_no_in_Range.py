sd =int(input("enter starting number"))
ed =int(input("enter ending number"))
for num in range(sd, ed):
    if(num ==1):
        continue
    for i in range(2, num):

     
        if num % i == 0:
            break

  
    else:
        print(num, end=" ")