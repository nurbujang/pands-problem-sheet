# es.py
# Author: Nur Bujang

# Week 7 task
# The task is to write a program that reads in a text file 
# and outputs the number of e's it contains. 
# It requires one to think about what is being asked here 
# and document any assumptions one makes. 
# The program should take the filename from an argument on the command line.

# $ python es.py moby-dick.txt

# 116960

# import argparse module
import argparse

# instantiate an ArgumentParse class instance
parser = argparse.ArgumentParser()

# call the argument 'FILENAME', remember, argument =things you pass data to a function without having to worry about what the data is
# when you store the arguments inside the function, it becomes a parameter (parameters = variables inside of the function used to store that data)
parser.add_argument('FILENAME')

# parse the argument(s)
args = parser.parse_args()

# access the 'FILENAME' argument
FILENAME = args.FILENAME

# open the file read-only
with open(FILENAME, 'r') as f:
    file_content = f.read()

# assume the starting point is upper-case 'CHAPTER 1', not 'Chapter 1'
start_content = file_content.split('CHAPTER 1') 

# declare ending_text, end BEFORE "End of this Project Gutenberg etext of Moby Dick, by Herman Melville"
ending_text = 'End of this Project Gutenberg etext of Moby Dick, by Herman Melville'

# assume the last element in the list has the ending_text
# split again and keep only the first portion
# overwrite this last element with the removed ending_text
start_content[-1] = start_content[-1].split(ending_text)[0]

# start with 0
e_counter = 0

# for each element in start_content, except the first one, count the 'E'
# don't distinguish between lower-case and upper-case E
for s in start_content[1:]:
    e = s.upper().count('E') # all text have been changed to upper case
    e_counter+=e
    
# add one for 'Chapter 1' that was used for splitting
e_counter+=1

# final answer
print(e_counter)

# number of 'e' from moby-dick.txt retrieved from this program is less than task instruction because it discounted texts before Chapter 1 and the last statement declared by the online publisher.