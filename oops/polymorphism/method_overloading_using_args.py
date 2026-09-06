class cal:
    def add( self,*args):
        sum =0
        for i in args:
            sum = sum +i 
     
        print(sum)      


a = cal()
a.add(1,2,3)    