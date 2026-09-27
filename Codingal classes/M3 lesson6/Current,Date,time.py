from datetime import date , time , datetime

# calling the today
# funtion of date class
today=date.today()
now = datetime.now
print("Today's date is:", today)
print("\nCurrent date and time is:", now)   


# printing date's components
print("\nDate component", today.year, today.month, today.day)
