from datetime import date, timedelta

today = date.today()

print(today.weekday())
f_date = today.strftime("%d- %m- %Y")
print(f_date)
expiry_date = today + timedelta(days=7)
print(expiry_date)