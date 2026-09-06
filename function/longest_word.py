from functools import reduce
words =["pyton","Dyango","java","javascript"]
a = reduce(lambda x,y:x.max() >y.max(),words)
print(a)