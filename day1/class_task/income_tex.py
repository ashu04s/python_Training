income =int(input("Enter your income: "))
if income <= 300000:
    tax = 0
elif income <= 500000:
    tax = (income - 300000) * (5 / 100)
    print("Tax amount is:", tax)
elif income <= 1000000:
    tax = (income - 500000) * (10 / 100) + 10000
    print("Tax amount is:", tax)
else:
    tax = (income - 1000000) * (20 / 100) + 60000
    print("Tax amount is:", tax)
    
print("Annual salary is:", income)   
print("net salary is:", income - tax)