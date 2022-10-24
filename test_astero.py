from naked import *
from datetime import datetime

# Testing passing empty asteroids list
print("Checking date format:")
print("----------")
print("Testing function: \get_todays_date\"")
if datetime.strptime(get_todays_date(), "%Y-%m-%d"):
    print("Date format is OK.")
else:
    print("Date is not OK.")
print("----------")

assert get_todays_date() == format('%Y-%m-%d')