from datetime import datetime, timedelta

# Take date input from user
date_string = input("Enter current date (YYYY-MM-DD): ")

# Convert string to datetime object
current_date = datetime.strptime(date_string, "%Y-%m-%d")

# Subtract 5 days
new_date = current_date - timedelta(days=5)

# Display results
print("Current Date:", current_date.date())
print("5 days before Current Date:", new_date.date())
