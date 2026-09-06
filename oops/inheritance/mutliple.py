

# parent  |   mother
#         |
#         |
#         |
#       child

# child class kini do mutliple class ki property inherit karega


class Father:
    def house(self):
        print("we have a house")

class Mother:
    def khaana(self):
        print("mother makes food")

class child(Father,Mother):
    def hello(self):
        print("hello from all0")
        
a = child()
a.hello()
a.khaana()
a.house()                