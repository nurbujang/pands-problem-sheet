# weekday.py
# Author: Nur Bujang

# Week 5 task
# to write a program that outputs whether or not today is a weekday. 
# I will need to search the web to find how you work out what day it is.

#An example of running this program on a Thursday is given below.

# Yes, unfortunately today is a weekday.

# An example of running it on a Saturday is as follows:

# It is the weekend, yay!

# import modules
import datetime

# put weekdays as a tuple
weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

weekday=datetime.datetime.today().isoweekday()
if weekday < 6:
    print("Yes, unfortunately today is a weekday")
# weekend, Sat is 6, Sun is 7
else:  
    print("It is the weekend, yay!")

