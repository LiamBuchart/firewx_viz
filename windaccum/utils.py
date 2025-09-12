"""

    Often required functions to grab

"""
from datetime import date, timedelta

def get_dates_in_year(year):
    start = date(year-1, 12, 1)
    end = date(year, 11, 30)
    delta = timedelta(days=1)
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime('%Y%m%d'))
        current += delta
    return dates