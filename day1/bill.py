bill = int(input("Enter the total bill amount: "))
if(bill<0 or bill>100):
   print('bill amount should be between 0 and 100')
elif(bill>=0 and bill<=100):
   tip = bill * 5
   print('Tip amount is:', tip)
else:
   tip = bill * 0.1
   print('Tip amount is:', tip)