from naked import *
from datetime import datetime
import re
import unittest

# Testing passing empty asteroids list
def test_date():
    print("Checking date format:")
    print("----------")
    print("Testing function: get_todays_date()")
    if datetime.strptime(get_todays_date(), "%Y-%m-%d"):
        print("Date format is OK.")
    else:
        print("Date is not OK.")
    print("----------")

    assert re.match('\\d{4}-\\d{2}-\\d{2}', get_todays_date())
