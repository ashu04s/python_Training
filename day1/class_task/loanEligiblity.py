age = int(input("Enter your age: "))
monthlyincome = int(input("Enter your monthly income: "))
creditscore = int(input("Enter your credit score: "))
if age >= 18 and monthlyincome >= 30000 and creditscore >= 750:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")   
    if age < 18:
        print(": Age is less than 18.")
    if monthlyincome < 30000:
        print(": Monthly income is less than 30000.")
    if creditscore < 750:
        print(" Credit score is less than 750.") 