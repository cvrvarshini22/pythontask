import datetime

def today_date():
    today = datetime.date.today()
    print("Date:", today.strftime("%d %B %Y, %A"))
