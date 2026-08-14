sd = int(input("enter starting range"))
ed = int(input("enter ending range"))
for st in range(sd, ed+1):
    arm = 0
    n = st
    temp=n
    length = len(str(n))
    while n > 0:
        rev = n % 10
        arm = arm+ rev ** length
        n //= 10
    if arm == temp:
        print(st)