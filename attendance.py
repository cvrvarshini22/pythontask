held = int(input("Enter number of classes held: ")) 
attended = int(input("Enter number of classes attended: "))  
percentage = (attended / held) * 100
if percentage < 75:
    print("Not Allowed to sit in exam")
else:
    print("Allowed to sit in exam")
