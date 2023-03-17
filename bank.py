# bank.py
# Author: Nur Bujang

# Weekly Task 2
# Banks store currency figures as integers (usually in cent) to avoid rounding errors
# This program should:
# prompt the user and read in two money amounts (in cent)
# add the two amounts
# print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount

# Enter amount1(in cent): 65
# Enter amount2(in cent): 180
# The sum of these is €2.45

# input is a string or a text, so convert it into numbers
int1=int(input("Enter amount1(in cent): "))
int2=int(input("Enter amount2(in cent): "))

# divide the sum with 100 to print it in euro and cent amount
# use / to divide into a float
ans=(int1+int2)/100

# print out the sentence in a new line (\n) in a string containing the answer in euro sign and number
# f or f-strings is formatted string literals, NOT a function. It is a new string formatting approach in Python 3.6 and above.
print(f"\nThe sum of these is \N{euro sign}{ans}")