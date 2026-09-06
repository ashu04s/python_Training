# give single result 

from functools import reduce
list = [1,2,4,5]
a = reduce(lambda x,y:x+y,list)
print(a)