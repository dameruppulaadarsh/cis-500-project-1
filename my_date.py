#######################################################
# my_date
#
# Name: Adarsh Dameruppula (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
print(is_leap_year(1984))
print(is_leap_year(1985))

days_in_every_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]  
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
    if is_leap_year(year):
        days_in_month[2] = 29
    ordinal_date = sum(days_in_month[:month]) + day
    return ordinal_date   
print(ordinal_date(1997, 1, 1))  
print(ordinal_date(1995, 2, 1))   


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    ordinal_date1 = ordinal_date(year1, month1, day1)
    ordinal_date2 = ordinal_date(year2, month2, day2)
    difference_between_years = year2 - year1
    if_it_is_leap_years = sum(1 for year in range(year1,year2) if is_leap_year(year))
    res = (difference_between_years * 365) + if_it_is_leap_years + (ordinal_date2 - ordinal_date1)
    return res

print(days_elapsed(1997, 1, 1, 1997, 1, 2))
print(days_elapsed(1997, 1, 1, 1997, 2, 1))
print(days_elapsed(1997, 1, 1, 1997, 1, 15))
  

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    for i in range(1, month):
        day += days_in_every_month[i]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month > 2:
            day += 1
    for x in range(1753, year):
        if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
            day += 366
        else:
            day += 365
    week_index = (day + 6) % 7
    return DAYS_OF_WEEK[week_index]
print(day_of_week(1753, 1, 1))
print(day_of_week(2023, 9, 29))


def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    months_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
    name_of_day = day_of_week(year, month, day)
    return f"{name_of_day}, {day:02d} {months_name[month - 1]} {year}"
print(to_str(2023, 10, 8))