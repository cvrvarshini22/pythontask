username = ("varshini","divya","varsha")
emailid = ("varshini@gmail.com", "divya33@gmail.com", "varsha5@gmail.com")
uname = input("enter your username: ")
mailid = input("enter your emailid: ")
if  uname in username:
    print("username is found")
elif uname in username:
    print("username is not found")
if  mailid in emailid:
    print("emailid is found")
elif mailid in emailid:
    print("emailid is not found")
else:
    print("invalid username or emailid")
