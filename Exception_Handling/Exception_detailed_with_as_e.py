# to see kya error aa rahi hai

try:
    n=int(input("enter a number"))
    number = int(n)
except ValueError as e:
    print("error",e)
else:
    print(number)        