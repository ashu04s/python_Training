#   Bundling data and methods together
#     and controlling access to data.
#  __variable private variable cannot access outside the class


class Bank:  # Class names traditionally use Capital letters
    def __init__(self, acc, balance):
        self.acc = acc
        self.__balance = balance  # Fixed: Now it is a private variable bound to the object

    def show_balance(self):
        # Accessing the private variable inside the class is allowed
        print(f"Your balance is: ${self.__balance}")     

# --- Demonstration ---
a = Bank(121, 3000)
a.show_balance() 

# ❌ This will NOT change the private variable anymore. 
# It just creates a brand new, unrelated public variable named 'balance'.
a.balance = 600  

# Let's verify what the actual private balance is now:
a.show_balance()  # Output will still show $3000, proving it is protected!

# ❌ Trying to print the private variable directly from outside will crash:
# print(a.__balance)  # AttributeError: 'Bank' object has no attribute '__balance'
