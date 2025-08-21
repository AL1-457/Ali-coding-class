import calendar

# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

#display the calender 
print(calendar.month(yy, mm))

print()