# cli for task1
from datetime import datetime, timedelta

def generate_dates(years):
    today = datetime.today()
    list_of_date = []
    for i in range(0, years*365):
        date = today + timedelta(days=i)
        list_of_date.append(date)
    return list_of_date

years=int(input(f"please enter the number years "))
list_of_dates=generate_dates(years)
for date in list_of_dates:
    print(date)