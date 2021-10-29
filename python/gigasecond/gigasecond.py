
from datetime import datetime, timedelta
def add_gigasecond(birth_date):
    new_time = birth_date + timedelta(seconds=10**9)
    return new_time
