"""

    Often required functions to grab

"""
from datetime import date, timedelta

def get_dates_in_year(year):
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    delta = timedelta(days=1)
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime('%Y%m%d'))
        current += delta
    return dates

def get_date_from_years(yearS, yearE, month, day):
    dates = []
    for year in range(yearS, yearE + 1):
        try:
            date_obj = date(year, month, day)
            dates.append(date_obj.strftime('%Y%m%d'))
        except ValueError:
            continue
    return dates


