
import datetime

# Get current date and time
now = datetime.datetime.now()

# Convert to timetuple
t = now.timetuple()

print("Current date and time:", now)
print("Current year:", t.tm_year)
print("Month of year:", t.tm_mon)
print("Week number of the year:", now.strftime("%U"))   # strftime still used for week number
print("Weekday of the week:", now.strftime("%A"))
print("Day of year:", t.tm_yday)
print("Day of the month:", t.tm_mday)
print("Day of week (number):", t.tm_wday)




import datetime

# Get current date and time
now = datetime.datetime.now()

print("Current date and time:", now)
print("Current year:", now.year)
print("Month of year:", now.month)
print("Week number of the year:", now.strftime("%U"))
print("Weekday of the week:", now.strftime("%A"))
print("Day of year:", now.strftime("%j"))
print("Day of the month:", now.day)
print("Day of week (number):", now.strftime("%w"))



















