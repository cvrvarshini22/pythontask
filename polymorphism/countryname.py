class country:
    def __init__(self, name):
        self.name = name
    def capital(self):
        print("every country has a capital city")
    def language(self):
        print("every country has an offical language")
class India(country):
    def capital(self):
        print("The capital of India is New Delhi")
    def language(self):
        print("The main language spoken in India is Hindi")
class USA(country):
    def capital(self):
        print("The capital of USA is Washington, D.C")
    def language(self):
        print("The main language spoken in USA is English")
class UK(country):
    def capital(self):
        print("The capital of UK is London")
    def language(self):
        print("The main language spoken in UK is English")
country_name = input("enter the country name (India/USA/UK): ")
if country_name.upper( ) == "INDIA":
    c = India("India")
elif country_name.upper( ) == "USA":
    c = USA("USA")
elif country_name.upper( ) == "UK":
    c = UK("UK")
else:
    print("Invalid country name")
    exit( )
print("\n country name:", c.name)
c.capital( )
c.language( )
    
    
    
    
