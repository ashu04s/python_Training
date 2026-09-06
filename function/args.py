#multiple arguments pass kar sakta hai

def greet(*args):
    print(args)
    
greet("Ashu","aryan")


def greet2(*args):
    for i in args:
        print(i)
        
greet2("ashu","Aryan","avinash")



def add(*args):
    count =0
    for i in args:
        count=count+i
    print(count)   


add(1,3,4,5)          