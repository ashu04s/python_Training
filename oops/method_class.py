class MyClass:
    def sayHello(self):
        print("hello wrold")
    
    def __init__(self):
        print("i am magic function")
# __init__() is automatically called when an object is created.

# for acess any method throw object we use self
obj = MyClass()
obj.sayHello()