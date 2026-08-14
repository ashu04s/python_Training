num = int(input("enter a no"))
seq = num*num
sum =0
temp = num
while(seq>0):
    rev = seq % 10
    sum = sum + rev
    seq =seq // 10
if( sum == temp ):
    print("yes neon number")
else:
    print("not a neon number")        