days = int(input("Enter the number of days: "))
years = days // 365 
weaks = (days % 365) // 7
days = (days % 365) % 7
print(f"{years} years, {weaks} weeks, and {days} days")