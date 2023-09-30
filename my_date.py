#######################################################
# my_date
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return  True
    else:
        return False
        
print(is_leap_year(2020))
pass    
    
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    days_in_every_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_every_month[2] = 29
    ordinal_date = sum(days_in_every_month[:month]) + day
    return ordinal_date   
print(ordinal_date(2023, 1, 1))     
pass


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
def is_leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return  True
    else:
        return False
def ordinal_date(year, month, day):
    days_in_every_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_every_month[2] = 29
    ordinal_date = sum(days_in_every_month[:month]) + day
    return ordinal_date   
def days_elapsed(year1, month1, day1, year2, month2, day2):
    ordinal_date1 = ordinal_date(year1, month1, day1)
    ordinal_date2 = ordinal_date(year2, month2, day2)
    difference_between_years = year2 - year1
    if_it_is_leap_years = sum(1 for year in range(year1,year2) if is_leap_year(year))
    return (difference_between_years * 365) + if_it_is_leap_years + (ordinal_date2 - ordinal_date1)
year1 = 2023
month1 = 1
day1 = 1
year2 = 2045
month2 = 9
day2 = 23

print(days_elapsed(year1, month1, day1, year2, month2, day2))

pass
      
    

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    days_in_a_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    total_days = (year - 1753) * 365
    total_days += day
    total_days += sum(days_in_a_month[:month])
    if month <= 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)): 
        total_days -= 1
    index_day = (total_days + 1) % 7    
    return DAYS_OF_WEEK[index_day]    
print(day_of_week(2022, 3, 12))

pass    
              
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""

pass
    
    
    
              
    