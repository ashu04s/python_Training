# **kwargs allows a function to accept any number of
# keyword arguments. and key and value pairs

def display(**kwargs):
    for i,j in kwargs.items():
     print(i,j)
    
display(name="ashu",age="20") 



def display2(**kwargs):
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")   

display2(name="Ashu",age=20)        