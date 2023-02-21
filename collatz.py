# collatz.py
# Author: Nur Bujang

# Week 4 task
# to write a program asks the user to input any positive integer 
# and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Example of it running:
# $ python collatz.py
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1

# Method 1
# posint = int(input("Please enter a positive integer:"))
# numbers=[]
# numbers.append(posint)
# while posint != 1:
#     temp_posint=None
#     if (posint %2) == 0:
#         temp_posint=posint//2
#         numbers.append(temp_posint)
        
#     else:
#         temp_posint=posint*3+1
#         numbers.append(temp_posint)
#     posint=temp_posint

# print(numbers)
# but numbers appear in []

# Method 2 - sep and without []
posint = int(input("Please enter a positive integer:"))
numbers=[]
numbers.append(posint)
while posint != 1:
    temp_posint=None
    if (posint %2) == 0:
        temp_posint=posint//2
        numbers.append(temp_posint)
        
    else:
        temp_posint=posint*3+1
        numbers.append(temp_posint)
    posint=temp_posint

for number in numbers:
    print("", number, sep=" ", end="")