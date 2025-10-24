from datetime import datetime

# Get current datetime
now = datetime.now()

# Convert to milliseconds
milliseconds = int(now.timestamp() * 1000)

print("Current time in milliseconds:", milliseconds)
