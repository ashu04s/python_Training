import datetime
try:
    datetime.date(2026,2,29)
    print("Valid date")
except ValueError:
    print("Invalid date")