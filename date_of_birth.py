def check_date(day, month, year):
    if type(day) is not int: return False
    if type(month) is not int: return False
    if type(year) is not int: return False
    if year<1900 or year>2022: return False
    if month<1 or month>12: return False
    if day<1 or day>31: return False
    if month==4 and month==6 and month==9 and month==11 and day>31: return False
    if month==2 and day>29: return False
    if month==2 and day==29 and year%4!=0: return False
    if month==2 and day==29 and year%4==0 and year%100==0 and year!=2000: return False
    return True
day=int(input('Day:'))
month=int(input('Month:'))
year=int(input('Year:'))
result=check_date(day,month,year)
print(result)