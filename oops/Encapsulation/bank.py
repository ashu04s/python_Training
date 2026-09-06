# self.accno in user and self.mpin in user[accno]
# to check key and check exist in the  dic without using loops


class Bank:
    balance = 0

    def __init__(self, Acc, pin):

        self.Acc = Acc
        self.pin = pin
        self.user = {"Ashu": "121", "Aryan": "111", "Avinash": "100"}
        if self.Acc in self.user and self.pin == self.user[self.Acc]:
            self.__show()
        else:
            print("invalid")

    def __show(self):

        print("""
                    Welcome to the bank!!!
                    1. for blaance check
                    2. for depsoit
                    3 for   withdraw
                    4. for change pin
                    5. for exit
               """)
        while True:
            choice = int(input("enter your choice"))
            if choice == 1:
                self.__showBalace()
            elif choice == 2:
                self.__deposit()
            elif choice == 3:
                self.__withdraw()
            elif choice == 4:
                self.__changepin()
            else:
                break

    def __showBalace(self):
        print(f" {self.Acc} balance is: {self.balance}")

    def __deposit(self):
        ammount = int(input("enter ammount to be deposite"))
        self.balance = self.balance + ammount
        self.__showBalace()

    def __withdraw(self):
        wi_ammount = int(input("enter ammount to be withdraw"))
        if wi_ammount > self.balance:
            print("you have low balance")
        else:
            self.balance = self.balance - wi_ammount
            self.__showBalace()

    def __changepin(self):
        new_pin = input("enter new pin")
        self.user[self.Acc] = new_pin
        print(f"user new pin is {self.user[self.Acc]}")


user = input("enter the account no").strip().capitalize()
pin = input("enter the pass.").strip()
a = Bank(user, pin)


# to more secure we can make our method private
