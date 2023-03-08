from datetime import datetime, timedelta

def generate_dates():
    today = datetime.today()
    print(today)
    list_of_date = []
    for i in range(0, 4*365):
        date = today + timedelta(days=i)
        list_of_date.append(date)
    return list_of_date

print(generate_dates())

