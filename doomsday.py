import random as _r
names={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

def isLeapYear(y):
    """Check if the given year is a leap year or not"""
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    else:
        return False

def monthDays(m,y):
    """Return the number of days of a given month, in a given year"""
    monthDays.days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if m==2 and isLeapYear(y):
        monthDays.days[m]=29
    return monthDays.days[m]

def nextDay(y,m,d):
    """Return the date of the next day"""
    day=(d%monthDays(m,y))+1
    month=m
    year=y
    if day==1:
            month=(m%12)+1
            if month==1:
                    year+=1
    return year,month,day

def doomsday(y):
    """Return the name of the doomsday"""
    doomsday.doom={1:3,2:28,3:14,4:4,6:6,7:4,8:8,10:10,12:12}
    if isLeapYear(y):
        doomsday.doom[1]=4
        doomsday.doom[2]=29
    anchor=[2,0,5,3]
    cent=(y//400)%4
    anchor_day=anchor[cent]
    diff=y-cent*100
    leap=0
    for year in range(cent*100+1,y+1):
        if isLeapYear(year):
            leap+=1
    dday=(anchor_day+diff+leap)%7
    doomsday.day={(doomsday.doom.get(n),n):dday for n in doomsday.doom}
    return dday

def what_day_is(d,m,y):
    """Return the name of the day"""
    anchor=doomsday(y)
    month=m
    year=y
    if doomsday.doom.get(m) is None:
        month-=1
    elif doomsday.doom.get(m) and doomsday.doom.get(m)>d and doomsday.doom.get(m-1) is None:
        month-=2
    if doomsday.doom.get(m) is not None and doomsday.doom.get(m)>d and m==1:
        month=12
        year=y-1
        anchor=doomsday(year)
    day=doomsday.doom.get(month)
    c=0
    while True:
        if not(day==d and month==m):
            day,month,year=nextDay(day,month,year)
            c+=1
            continue
        else:
            break
    final_day=(c + anchor)%7
    return names[final_day]

def randDay(start, end):
    """(year, month, day) to (year, month, day)"""
    y = _r.randint(start[0],end[0])
    if y==start[0]:
        m = _r.randint(start[1],12)
    elif y==end[0]:
        m = _r.randint(1,end[1])
    else:
        m = _r.randint(1,12)
    md = monthDays(m, y)
    if m==start[1]:
        d = _r.randint(start[2],md)
    elif m==end[1]:
        d = _r.randint(1,end[2])
    else:
        d = _r.randint(1,md)
    return y,m,d

def unlucky_year(y):
    """Return the number of friday's the 13th on that year"""
    year=y
    day=1
    month=1
    c=0
    while year<y+1:
        day,month,year=nextDay(day,month,year)
        if what_day_is(day,month,year)=='Friday' and day==13:
            c+=1
    return c

def hours_to_decimal(s):
    s = s.split(":")
    if len(s) == 1: return int(s[0])
    elif len(s) == 2: return int(s[0])+int(s[1])/60
    else: return int(s[0])+int(s[1])/60+int(s[2])/3600

class Time:
    def __init__(self, val):
        self.val = val