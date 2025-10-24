from datetime import datetime

# Take input from the user
date_string = input("Enter date and time (e.g., July 1 14 2:43PM): ")

# Convert string to datetime object
date_object = datetime.strptime(date_string, "%B %d %y %I:%M%p")

# Display the result
print("Converted datetime:", date_object)
