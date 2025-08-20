from datetime import date , datetime

#calling the today
#function of date class\
today = date.today()
now = datetime.now()

print("Today's date is" , today)
print("Current date and time is" , now)
print()

#printing date's components
print("Date components", today.year, today.month, today.day)
print()