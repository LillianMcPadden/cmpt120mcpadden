# date.py
# This program accepts a date as month/day/year and then calculates the
# corresponding day number

def main():

    date = (input("Enter a date (mm/dd/yyyy): "))
    month, day, year = date.split('/')
    month = int(month)
    day = int(day)
    year = int(year)
    dayNum = 0
    
    if month == 4 or month == 6 or month == 9 or month == 11:
        if year % 4 == 0 or year % 100 == 0 and year % 400 != 0:
            dayNum = dayNum + ((day + 31 * (month-1)) - (((4 * month) + 23)//10) + 1)
        else:
            dayNum = dayNum + ((day + 31 * (month-1)) - (((4 * month) + 23)//10))
    if month == 2:
        if year % 4 == 0 or year % 100 == 0 and year % 400 != 0:
            dayNum = dayNum + (31 * (month-1) + day) + 1
        else:
            dayNum = dayNum + (day + 31 * (month-1))
    if month == 1:
        dayNum = 31 * (month-1) + day
    if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if year % 4 == 0 or year % 100 == 0 and year % 400 != 0:
            dayNum = dayNum + ((day + 31 * (month-1)) - (((4 * month) + 23)//10) + 1)
        else:
            dayNum = dayNum + ((day + 31 * (month-1)) - (((4 * month) + 23)//10))
    print('day number', dayNum, "in year", year)
main()
