# class cal:
#     def add(self,a,b):
#         return a+b;
#     def add(self,a,b,c):
#         return a+b+c;
    
# a = cal()
# print(a.add(1,3))    here second add function override first add function
# print(a.add(1,3,4))    
 

class cal:
    def add(self, a=None,b=None,c=None):
        if a is not None and b is not None and c is None:
            print(f"sum of ={a+b}")
        elif a is not None and b is not None and c is not None:
            print(f"sum of ={a +b+c}")

a = cal()
print(a.add(1,2,3))
            
                