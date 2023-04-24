Leap Year Checker
This Python script is a simple program that determines whether a given year is a leap year or not, based on the Gregorian calendar.

How to Use
To use this script, you need to have Python installed on your machine. To run the script, navigate to the directory where the script is saved and type the following command in your terminal:
		python leapyear.py
This will run the script and prompt you to enter a year to check if it is a leap year.

How it Works
The script defines a function called isALeapYear(year) which takes in a year as an argument and returns a boolean value indicating whether the year is a leap year or not. The function checks if the year is divisible by 4, and if it is, it checks if the year is not divisible by 100 or if it is divisible by 400. If the year meets these conditions, then it is a leap year.

The main() function prompts the user to enter a year to check, and then calls the isALeapYear(year) function to determine whether the year is a leap year or not. If the year is a leap year, it prints a message indicating that the year is a leap year. If the year is not a leap year, it prints a message indicating that the year is not a leap year and the reason why.

The script also includes a check to ensure that the main() function is only called if the script is being run as the main program, and not if it is being imported as a module.

Contribution
If you would like to contribute to this project, feel free to submit a pull request with your changes or suggestions.