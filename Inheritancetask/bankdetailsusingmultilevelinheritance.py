class Personal:
    def __init__(self):
        self.name = input("enter the name:    ")
        self.mail = input("enter the mail:  ")
        self.mobile = input("enter the mobile number:    ")
        self.address = input("enter the address:     ")
    def display_personal(self):
       print("/n--- Personal Information ---")
       print("Name                  :", self.name)
       print("Email                  :", self.mail)
       print("Mobile                :", self.mobile)
       print("Address               :", self.address)
class Educational(Personal):
    def __init__(self):
        super( ).__init__( )
        self.m1 = int (input("Enter the mark 1:   "))
        self.m2 = int (input("Enter the mark 2:    "))
        self.m3 = int (input("Enter the mark 3:    "))
        self.total = self.m1 + self. m2 + self.m3 
        self.percentage = self.total / 3
    def display_education(self):
        print("\n--- Education Information ---") 
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total Marks  :", self.total)
        print("percentage     :", round(self.percentage, 2), "%")
class Bank(Educational):
    def __init__(self):
        super( ).__init__( )
        self.accnum = input("Enter the Account number:    ")
        self.branchname = input("Enter the Branch Name:   ")
        self.bankname = input("Enter the Bank Name:      ")
        self.ifsccode = input("Enter the IFSC Code:       ")
        self.availablebalance = float(input("Enter the Available Balance:    "))
    def display_bank(self):
        print("\n--- Bank Information ---")
        print("Account Number       :", self.accnum)
        print("Branch Name             :", self.branchname)
        print("Bank Name                :", self.bankname)
        print("IFSC Code                 :", self.ifsccode)
        print("Available Balance      :", self.availablebalance)

object = Bank( )

object.display_personal( )
object.display_education( )
object.display_bank( )
