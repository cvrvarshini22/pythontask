from datetime import date

# Take user's birth date as input
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Get today's date
today = date.today()

# Calculate age
age = today.year - birth_year

# Check if birthday has not occurred yet this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Display result
print("\nToday's Date:", today.strftime("%d-%m-%Y"))
print("Your Date of Birth:", f"{birth_day:02d}-{birth_month:02d}-{birth_year}")
print("Your Age:", age, "years")
