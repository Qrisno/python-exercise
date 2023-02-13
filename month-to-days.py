#Exercise 15

def calcMonthToDays(month):
    if month == "February":
        return "28 or 29 days"
    elif month in ("April", "June", "September", "November"):
        return "30 days"
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
	    return "31 days"

month = input("name of Month: ")

print(calcMonthToDays(month))

