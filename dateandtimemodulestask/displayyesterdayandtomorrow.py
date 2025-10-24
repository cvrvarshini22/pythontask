from datetime import date, timedelta

# Get today's date
today = date.today()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\n Display results:")
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)





from datetime import date, timedelta

# Get today's date
today = date.today()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Display all with date, month, and year")
print("Yesterday:", yesterday.strftime("%d-%m-%Y"))
print("Today    :", today.strftime("%d-%m-%Y"))
print("Tomorrow :", tomorrow.strftime("%d-%m-%Y"))
