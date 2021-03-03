import calendar
year = int(input("Enter the year for which you want to see the month:"))
month = int(input("Enter the month you want to see:"))
print(calendar.month(year, month))
day = int(input("Enter the day you want to see:"))
dayname = calendar.weekday(year, month, day)
if dayname == 0:
    print("Monday")
elif dayname == 1:
    print("Tuesday")
elif dayname == 2:
    print("Wednesday")
elif dayname == 3:
    print("Thursday")
elif dayname == 4:
    print("Friday")
elif dayname == 5:
    print("Saturday")
else:
    print("Sunday")
