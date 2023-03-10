# squareroot.py
# Author: Nur Bujang

# Week 6 task
# to write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# I should create a function called <tt>sqrt</tt> that does this.
# I am to create my own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
# The newton method at estimating square roots was suggested.

# $ python squareroot.py
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.

# the Newton Method square root approximation formula
# newtsqrt = 0.5*(guess+(flonum/guess)), let flonum be any number, and guess is the approximation of the square root of flonum

flonum=float(input("Please enter a positive number: ")) # prompt to input a positive float number

def newtsqrt(flonum): # define the function newtsqrt with 1 argument flonum
    guess=0.5*flonum # variable declaration to get the square root of flonum ONLY
    better=0.5*(guess+flonum/guess)  # variable declaration to calculate a better approximation of guess
    while better!=guess: # while loop, as long as better is not equal to guess
        guess=better # this is to hold the value
        better=0.5*(guess+flonum/guess)  # updating the guess
    return round(better,1) # return number and round up to 1 decimal point
print(f"The square root of {flonum} is approx. {newtsqrt(flonum)}.") # call function
