class Humman:
    def walk(self):
        print("human walk with two legs")

class Animal(Humman):
    def walk(self):
        print("animal walk with four legs")       


a = Animal()
b =Humman()
a.walk()   
b.walk()     