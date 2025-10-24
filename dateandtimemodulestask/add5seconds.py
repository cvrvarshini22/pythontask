from datetime import datetime, timedelta

# Get current date and time
current_time = datetime.now()

# Add 5 seconds
new_time = current_time + timedelta(seconds=5)

# Display results
print("Current Time:", current_time.strftime("%d-%m-%Y %I:%M:%S%p"))
print("After adding 5 seconds:", new_time.strftime("%d-%m-%Y %I:%M:%S%p"))



