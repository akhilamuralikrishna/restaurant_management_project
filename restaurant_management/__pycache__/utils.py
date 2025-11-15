import datetime
weekly_hours={
    'Monday':('9:00 AM','9:00 PM')
    'Tuesday':('9:00 AM','9:00 PM')
    'Wednesday':('9:00 AM','9:00 PM')
    'Thursday':('9:00 AM','9:00 PM')
    'Friday':('9:00 AM','11:00 PM')
    'Saturday':('10:00 AM','11:00 PM')
    'Sunday': None
}
today=datetime.datetime.today().strftime('%A')
hours=weekly_hours.get(today)

if hours is None:
    reurn None
return hours    