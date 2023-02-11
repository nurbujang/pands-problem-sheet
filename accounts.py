# accounts.py
# Author: Nur Bujang

# Week 3 task
# Bank account numbers can be stored as 10 character strings.
# For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs)
# This task is to write a python program called accounts.py that reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

## $ python accounts.py
## Please enter an 10 digit account number: 1234567890
## XXXXXX7890

# Extra: To modify the program to deal with account numbers of any length (a vague requirement, comment my assumptions)

# create prompt to enter a 10-digit account number
# Remember the account number is a string
input_string=input("Please enter an 10 digit account number: ")

# slice string to replace the first 6 numbers with X and display only the last 4 digits of the account number
# replacement="XXXXXX"
# output_string=input_string.replace(input_string[0:6],replacement,1)
# print(output_string)

# or
replacements=(len(input_string)-4)*"X"
display=input_string[-4:]
print(replacements+display)


# To modify the program to deal with account numbers of any length (a vague requirement, comment my assumptions)
input_string=input("Please enter your account number: ")
# slice the string into 2: replacement and display
replacements=(len(input_string)-4)*"X" # replace length(all-4), which is an unknown number, with X, because A STRING IS A LIST
## (len(input_string)-4) is a NUMBER
## "X" is a STRING

display=input_string[-4:] # display the last 4 digits
print(replacements+display)

# Different account number lengths could be due to:
## the date when the account was opened, ie. older accounts are shorter, newer accounts are longer
## the country where the account was opened, eg: Ireland uses IBAN, USA uses ABA routing transit numbers, Malaysia uses SWIFT code.
## branch code/sort code
## routing codes



