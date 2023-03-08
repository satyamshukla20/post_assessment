# cli for task2
from datetime import  timedelta
import datetime
def create_dates(begin_date, end_date):
    dates = []
    today_date = begin_date
    while today_date <= end_date:
        dates.append(today_date)
        today_date += timedelta(days=1)
    return dates

begin_date = input(f"please enter begin date in this format (dd/mm/yyyy)")
begin_date=datetime.datetime.strptime(begin_date,"%d/%m/%Y").date()
end_date = input(f"please enter end date in this format (dd/mm/yyyy)")
end_date=datetime.datetime.strptime(end_date,"%d/%m/%Y").date()
dates = create_dates(begin_date, end_date)

for date in dates:
    print(date)
