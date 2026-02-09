from datetime import datetime, timedelta

def get_time():
    return datetime.now().strftime("%H:%M.%d.%m.%y")

def get_date():
    return datetime.now().strftime("%d.%m.%Y")

def get_week(date):
    dt = datetime.strptime(date, "%H:%M.%d.%m.%y")
    return dt.isocalendar().week

def calculate_time(start):
    now = datetime.strptime(get_time(), "%H:%M.%d.%m.%y")
    start_time = datetime.strptime(start, "%H:%M.%d.%m.%y")

    if start_time > now:
        diff = now + timedelta(days=1) - start_time
    else:
        diff = now - start_time

    hour = str(round(diff.total_seconds() / 3600, 2)).replace(".", ",")
    return hour

