import math
import calendar

month_numbers = {
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "january": 13,
    "february": 14
}

week_days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

try:
    year = int(input("What year were you born in? "))
except ValueError:
    exit("You must enter a valid year.")

month = input("What month were you born in? (Enter a number or name): ")

if month.isdigit() and 1 <= int(month) <= 12:
    month_number = int(month)
elif month.lower() in month_numbers.keys():
    month_number = month_numbers[month.lower()]
else:
    exit("You must input a valid month.")

try:
    day = int(input("What day were you born in? "))

    if not 1 <= day <= 31:
        raise ValueError("invalid range")
except ValueError:
    exit("You must input a valid day.")

if calendar.isleap(year) and month_number == 14 and day > 29:
    exit(f"{year} is a leap year and February was selected; you must enter a day that is 29 or under.")
elif not calendar.isleap(year) and month_number == 14 and day > 28:
    exit("That month only has 28 days.")
elif month_number in [4, 6, 9, 11] and month_number > 30:
    exit("That month only has 30 days.")

if month_number in [13, 14]:
    # January is the 13th month of the last year, and february is the 14th
    year -= 1

K = year % 100
J = year // 100

result = math.floor((day + ((13 * (month_number + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7)
print(f"You were born on a {week_days[result]}.")
