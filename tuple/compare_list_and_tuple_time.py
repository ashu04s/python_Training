import time
l1 =list(range(1000))
ls= time.time()
for i in l1:
    pass
le =time.time()
print("list time",le-ls)


tuple =tuple(range(1000))
ts=time.time()
for i in tuple:
    pass
te =time.time()
print("time taken by tuple",te-ts)

