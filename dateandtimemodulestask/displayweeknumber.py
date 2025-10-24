import datetime

# Take input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Create a date object
given_date = datetime.date(year, month, day)

# Get the week number (%U gives week number of year)
week_number = given_date.strftime("%U")

print("Sample Date:", given_date)
print("Week Number of the year:", week_number)
