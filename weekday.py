# weekday.py
# Author: Nur Bujang

# Week 5 task
# to write a program that outputs whether or not today is a weekday. 
# I will need to search the web to find how you work out what day it is.

#An example of running this program on a Thursday is given below.

# Yes, unfortunately today is a weekday.

# An example of running it on a Saturday is as follows:

# It is the weekend, yay!

# import module
import datetime

weekday=datetime.datetime.today().isoweekday() # module.class.argument.function within datetime
# use if else because it's either weekday or weekend only
if weekday < 6:   # in isoweekday, Mon-Fri are designated as 1-5
    print("Yes, unfortunately today is a weekday")
else:  # in isoweekday, weekends, Sat is 6, Sun is 7
    print("It is the weekend, yay!")

