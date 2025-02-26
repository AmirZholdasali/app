import datetime

x = datetime.datetime(2025, 2, 23, 20, 26, 50)
y = datetime.datetime(1465, 9, 7, 16, 43, 23)
z = int((x - y).total_seconds())
print(z)