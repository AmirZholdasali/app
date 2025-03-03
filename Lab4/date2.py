import datetime

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"todays date is {today}")
print(f"yesterday was {yesterday}")
print(f"tomorrow will be {tomorrow}")