# easter.py
# this program inputs a year, verifies that it is in the proper range, and
# then prints out the date of Easter that year

def main():
    year = eval(input("Enter year here: "))
    if year >= 1982 and year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
        if date > 31:
            date = date - 31
            print("Easter in the year", year, "is on April", date)
        else:
            print("Easter in the year", year, "is on March", date)
    else:
        print("Year out of range")
main()
    
