from datetime import date
d1 = input("Please insert the first date in the following format yyyy/mm/dd:")
d2 = input("Please insert the second date in the following format yyyy/mm/dd:")
date1 = d1.split("/")
date2 = d2.split("/")
d1 = date(int(date1[0]), int(date1[1]), int(date1[2]))
d2 = date(int(date2[0]), int(date2[1]), int(date2[2]))
diff = d1 - d2
print(abs(diff.days))
