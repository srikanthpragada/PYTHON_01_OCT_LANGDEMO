month = int(input("Enter month : "))
if month == 2:
    year = int(input("Enter year : "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        nd = 29
    else:
        nd = 28
elif month in (4, 6, 9, 11):
    nd = 30
else:
    nd = 31

print("No. of days : ", nd)
