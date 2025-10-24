from datetime import date

# Define a function to add years
def addYears(d, years):
    try:
        # Replace the year directly
        return d.replace(year=d.year + years)
    except ValueError:
        # Handle leap year case (e.g., Feb 29)
        return d.replace(month=2, day=28, year=d.year + years)

# Test cases
print("Updated Dates:")
print(addYears(date(2015, 1, 1), -1))   # One year before 2015
print(addYears(date(2015, 1, 1), 0))    # Same year
print(addYears(date(2015, 1, 1), 2))    # Two years later
print(addYears(date(2000, 2, 29), 1))   # Leap year handling
