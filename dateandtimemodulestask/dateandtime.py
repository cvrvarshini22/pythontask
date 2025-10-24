from datetime import datetime
date_string = input("enter the date in format (dd-mm-yyyy): ")
date_object =datetime.strptime(date_string, "%d %B %Y")
print("converted datetime object:",date_object)
