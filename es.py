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

FILENAME="moby-dick.txt"
with open(FILENAME, 'r') as f:
    file_name_data = f.read()
    
# start AFTER "WHALE SONG."

start=find('WHALE SONG.'+1)

# end BEFORE "End of this Project Gutenberg etext of Moby Dick, by Herman Melville"
end=find('End of this Project Gutenberg etext of Moby Dick, by Herman Melville'-1)

import argparse
#create an argument object
parser = argparse.ArgumentParser(description='Process some integers.') 
# make calls to the add_argument() method
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
