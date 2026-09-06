# privated = __varible
# ya to class ka ander acess ho sakta hai 

# protect =_
# jisko permission dega 
# like class Result(Demo) 

class Demo():
    __college ="miet"
    _age =20
    def student(self,name):
        self.name =name
        
a = Demo()
a.student("ashu")
print(a.name)
a.name="abinash" #public modifier        
print(a.name)
print(a._age)
print(a._college)



