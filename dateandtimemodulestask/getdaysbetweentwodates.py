from datetime import date

# Take input from the user
y1 = int(input("Enter start year: "))
m1 = int(input("Enter start month: "))
d1 = int(input("Enter start day: "))

y2 = int(input("Enter end year: "))
m2 = int(input("Enter end month: "))
d2 = int(input("Enter end day: "))

# Create date objects
start_date = date(y1, m1, d1)
end_date = date(y2, m2, d2)

# Find the difference
difference = end_date - start_date

# Display the result
print("Start Date:", start_date)
print("End Date:", end_date)
print("Difference:", difference)
