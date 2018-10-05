
month = int(input("Enter month : "))
if month == 2:
    nd = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    nd = 30
else:
    nd = 31


print("No. of days : ", nd)


