# Author: Miguel Ibarra【=◈︿◈=】
def isALeapYear(year):
# A year is a leap year if it is divisible by 4,
# but not divisible by 100 unless it is also divisible by 400
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def main():
    year = int(input('Enter a year to check if it is a leap year: '))

    if isALeapYear(year):
        print(str(year) + ' is a leap year')
    else:
        if year % 100 == 0 and year % 400 != 0:
            print(str(year) + ' is not a leap year, as it is divisible by 100 but not by 400')
        else:
            print(str(year) + ' is not a leap year')

# If leapyear.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()