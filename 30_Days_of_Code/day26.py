# Enter your code here. Read input from STDIN. Print output to STDOUT

day, month, year = input().split()
due_day, due_month, due_year = input().split()

day = int(day)
month = int(month)
year = int(year)
due_day = int(due_day)
due_month = int(due_month)
due_year = int(due_year)

calc_year = year - due_year
calc_month = month - due_month
calc_day = day - due_day


#tuple comparison
if (year, month, day) <= (due_year, due_month, due_day):
  print(0)
elif (year, month) == (due_year, due_month):
  print(15*calc_day)
elif year == due_year:
  print(500*calc_month)
else:
  print(10000)
