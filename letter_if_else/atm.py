# atm machine
atm = int(input("enter your  atm number"))
pin = int(input("enter your pin"))
balance = 1000
if atm == 12345:
    if pin == 123:
        while True:
            print("welcome to sbi atm")
            print("1. please check your balance")
            print("2. please deposit \n amount")
            print("3. please withdraw amount")
            print("4. please change your pin")
            print("0. exit")
            choice = int(input("enter your choice: "))
            if choice == 1:
                print("your balance is", balance)
            elif choice == 2:
                amount = int(input("enter deposit amount: "))
                balance += amount
                print("updated balance is", balance)
            elif choice == 3:
                amount = int(input("enter withdraw amount: "))
                if amount <= balance:
                    balance -= amount
                    print("please collect your cash")
                    print("remaining balance is", balance)
                else:
                    print("insufficient balance")
            elif choice == 4:
                new_pin = int(input("enter new pin: "))
                pin = new_pin
                print("pin changed")
            elif choice == 0:
                print("thank you")
                print("thanks for coming")
                break
            else:
                print("invalid choice")
    else:
        print('invalid pin')
else:
    print("invalid atm number")