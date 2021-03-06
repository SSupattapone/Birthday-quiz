"""
birthday.py
Author: Sam Supattapone
Credit: none
Assignment: Birthday

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? " .format(name))
year = input("And what year were you born in, {0}? " .format(name))
day = input("And the day? ")

if month == "October" and int(day) == 31:
    print("You were born on Halloween!")

elif month == month_name[todaymonth] and int(day) == todaydate:
    print("Happy birthday!")

elif int(year) < 1980 and (month == "December" or month == "January" or month == "February"):
    print("{0}, you are a winter baby of the Stone Age." .format(name))
elif int(year) < 1980 and (month == "March" or month == "April" or month == "May"):
    print("{0}, you are a spring baby of the Stone Age." .format(name))
elif int(year) < 1980 and (month == "June" or month == "July" or month == "August"):
    print("{0}, you are a summer baby of the Stone Age." .format(name))
elif int(year) < 1980 and (month == "September" or month == "October" or month == "November"):
    print("{0}, you are a fall baby of the Stone Age." .format(name))

elif 1980 <= int(year) <= 1989 and (month == "December" or month == "January" or month == "February"):
    print("{0}, you are a winter baby of the eighties." .format(name))
elif 1980 <= int(year) <= 1989 and (month == "March" or month == "April" or month == "May"):
    print("{0}, you are a spring baby of the eighties." .format(name))
elif 1980 <= int(year) <= 1989 and (month == "June" or month == "July" or month == "August"):
    print("{0}, you are a summer baby of the eighties." .format(name))
elif 1980 <= int(year) <= 1989 and (month == "September" or month == "October" or month == "November"):
    print("{0}, you are a fall baby of the eighties." .format(name))

elif 1990 <= int(year) <= 1999 and (month == "December" or month == "January" or month == "February"):
    print("{0}, you are a winter baby of the nineties." .format(name))
elif 1990 <= int(year) <= 1999 and (month == "March" or month == "April" or month == "May"):
    print("{0}, you are a spring baby of the nineties." .format(name))
elif 1990 <= int(year) <= 1999 and (month == "June" or month == "July" or month == "August"):
    print("{0}, you are a summer baby of the nineties." .format(name))
elif 1990 <= int(year) <= 1999 and (month == "September" or month == "October" or month == "November"):
    print("{0}, you are a fall baby of the nineties." .format(name))

elif 2000 <= int(year) and (month == "December" or month == "January" or month == "February"):
    print("{0}, you are a winter baby of the two thousands." .format(name))
elif 2000 <= int(year) and (month == "March" or month == "April" or month == "May"):
    print("{0}, you are a spring baby of the two thousands." .format(name))
elif 2000 <= int(year) and (month == "June" or month == "July" or month == "August"):
    print("{0}, you are a summer baby of the two thousands." .format(name))
elif 2000 <= int(year) and (month == "September" or month == "October" or month == "November"):
    print("{0}, you are a fall baby of the two thousands." .format(name))