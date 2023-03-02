# collatz.py
# Author: Nur Bujang

# Week 4 task
# to write a program that asks the user to input any positive integer 
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
# numbers=[]                    # numbers will be in a list
# numbers.append(posint)        # the first number to append
# while posint != 1:
#     temp_posint=None          # for temporary storage bc we have to declare a variable somewhere
#     if (posint %2) == 0:
#         temp_posint=posint//2
#         numbers.append(temp_posint)
        
#     else:
#         temp_posint=posint*3+1
#         numbers.append(temp_posint)
#     posint=temp_posint        # because it's a whole series/sequence

# print(numbers)
# but numbers appear in []

# Method 2 - using sep and without []
posint = int(input("Please enter a positive integer:"))
numbers=[]                   # numbers will be in a list
numbers.append(posint)       # the first number to append
while posint != 1:
    temp_posint=0    # or None, for temporary storage bc we have to declare a variable somewhere
    if (posint %2) == 0:
        temp_posint=int(posint/2)
        numbers.append(temp_posint)
        
    else:
        temp_posint=int(posint*3+1)
        numbers.append(temp_posint)
    
    posint=temp_posint      # because it's a whole series/sequence of numbers

for number in numbers:
    print("", number, sep=" ", end=" ")




