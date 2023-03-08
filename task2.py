from datetime import datetime, timedelta

def create_dates(begin_date, end_date):
    dates = []
    today_date = begin_date
    while today_date <= end_date:
        dates.append(today_date)
        today_date += timedelta(days=1)
    return dates

begin_date = datetime(2023, 6, 3).date()
end_date = datetime(2023, 6, 23).date()
dates = create_dates(begin_date, end_date)
print(dates)


