year = int(input("Enter a number: "))
if year%4 == 0:
  if year%100 == 0 and year%400 != 0:
    print("Year " + str(year) + " is not a leap year.")
  else:
    print("Year " + str(year) + " is a leap year.")
else:
  print("Year " + str(year) + " is not a leap year.")