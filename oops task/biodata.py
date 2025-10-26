from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%d-%m-%Y").date()

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

# Example
p = Person("Chitra", "India", "25-05-1982")
print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.age(), "years")
