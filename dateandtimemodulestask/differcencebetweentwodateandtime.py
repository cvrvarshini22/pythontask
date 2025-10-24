from datetime import datetime

# Take input from the user
print("Enter first date and time:")
date1_str = input("Format (YYYY-MM-DD HH:MM:SS): ")

print("Enter second date and time:")
date2_str = input("Format (YYYY-MM-DD HH:MM:SS): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate the difference
difference = date2 - date1

# Extract total seconds
total_seconds = difference.total_seconds()

# Convert to days, hours, minutes, seconds
days = difference.days
hours = int((total_seconds % (24 * 3600)) // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)

# Display the results
print("\nDifference between the two dates:")
print(f"Days   : {days}")
print(f"Hours  : {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
