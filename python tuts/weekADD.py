#weekADD.py
from datetime import datetime, timedelta

# Given date
start_date = datetime.strptime('02-09-2024', '%d-%m-%Y')

# Adding 16 weeks (16 weeks * 7 days per week)
weeks_to_add = 16
new_date = start_date + timedelta(weeks=weeks_to_add)

new_date.strftime('%d-%m-%Y')
print(new_date)#print date
