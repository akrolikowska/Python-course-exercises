import datetime
import time

try:
    year = int(input("Podaj rok: "))
    month = int(input("Podaj miesiąc: "))
    day = int(input("Podaj dzień: "))
except ValueError:
    print("Podałeś nienumeryczną wartość lamusie dlatego ustawiam datę swoich urodzin i oczekuję na prezent")
    year = 1996
    month = 1
    day = 1

while year <= 0:
    year = int(input("Podaj rok większy od 0: "))
while month <=0 or month>12:
    month = int(input("Podaj miesiąc większy od 0 i mniejszy od 12"))
while day<=0 or day>31 or (month in [4,6,9,11] and day==31) or (month in [2] and day>28):
    day = int(input("Podaj poprawną ilość dni dla wybranego miesiąca: "))

date = datetime.date(year,month,day)
day_of_year = (date - datetime.date(date.year, 1, 1)).days + 1
print(day_of_year)
calendar = datetime.date.isocalendar(date)
week = calendar[1]
print(week)

result = day_of_year%7
if result == 0:
    week = day_of_year//7
else:
    week = day_of_year//7 +1
print(week)


newDate = date + datetime.timedelta(days=14)
print(newDate)

newDate2 = date - datetime.timedelta(days=14)
print(newDate2)

sunday = date + datetime.timedelta(6-date.weekday())
print("sunday: "+ str(sunday))

now = time.localtime()
print(now)
unixDate= datetime.datetime(year, month, day, now.tm_hour, now.tm_min, now.tm_sec)
print("data unixowa: " + str(unixDate))
czasUnixowy = unixDate.timestamp()
print("Czas unixowy: " + str(czasUnixowy))