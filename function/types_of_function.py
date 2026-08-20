# 1. user define function
# 2. predefine function


# function as first-class citizen
    # we store function in another varible and call that variable to exeute that 
    # function
def greet():
   print("hello ladle")

   
ashu = greet

ashu()

#higger order function return ma another function return karega
def hello():
    return a()

def a():
    print("hello bro!!")

hello()    
   