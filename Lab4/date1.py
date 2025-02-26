from datetime import datetime, timedelta

x = datetime.today()
y = x - timedelta(days=5)

print(f"todays date: {x}")
print(f"date 5 days ago: {y}")