from datetime import datetime as date

input_date = input()

d1 = date.strptime(input_date, "%Y-%m-%d").date()
d2 = date.strptime('2018-08-26', "%Y-%m-%d").date()

if d1 < d2:
    print("Passed")
elif d1 > d2:
    print(f"{(d1 - d2).days + 1} days left")
else:
    print("Today date")
