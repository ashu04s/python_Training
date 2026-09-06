# Abstraction means hiding unnecessary implementation details
# and exposing essential functionality.

# Example:

# ATM:

#     withdraw()
#     deposit()
#     check_balance()


# User does not need to know internal implementation.

from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound():
        pass

class Dog(Animal):
    def sound(self):
        print("dogs is barking")

class Cat(Animal):
    def sound(self):
        print("cat is meow")   
        
a = Cat()
a.sound()          