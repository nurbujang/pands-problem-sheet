# pands-problem-sheet
Problem sheet for Programming and Scripting

## **WEEK 1 TASK: helloworld.py**

### Task 1 Description:
*1. To create a python program that displays Hello World! when it is run then add, commit and push it into the pands-problem-sheet repository*

*2. To create a Github account containing two repositories: mywork (personal use) and pands-problem-sheet (for assessment)* 

*3. To make entries in README using markdown*

### Method:
1. Using VS Code, pands folder was created under the computer directory.
2. 3 subfolders were created under pands: a. mywork  b. pands-course-material  c. pands-problem-sheet
3. helloworld.py file was created under pands-problem-sheet. Comments were added to describe the code.
4. Code format followed that of (1).
5. Python print() function was used to create a string output onto the screen (2).
6. Python quote function was used for string representation (3).
7. Python bracket function indicates that round brackets are generally used in function (4).

### Conclusion:
Python program that displays Hello World! in the terminal was created, added, committed and pushed into https://github.com/nurbujang/pands-problem-sheet then submitted.

### References:
1. https://www.w3schools.com/python/
2. https://www.w3schools.com/python/ref_func_print.asp
3. https://www.geeksforgeeks.org/single-and-double-quotes-python/#:~:text=Generally%2C%20double%20quotes%20are%20used,one%20type%20over%20the%20other
4. https://stackoverflow.com/questions/30700603/different-meanings-of-brackets-in-python

## **WEEK 2 TASK: bank.py** 

### Task 2 Description:
*Banks store currency figures as integers (usually in cent) to avoid rounding errors. This task is to create a program that should prompt the user and read in two money amounts (in cent), then add the two amounts and finally print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.*

*Enter amount1(in cent): 65

Enter amount2(in cent): 180*


*The sum of these is €2.45*

### Method:
1. First is to define and prompt amount1. Input is a string or text, so it had to be converted into numbers (1). The same was done for amount2.
2. I divided the sum with 100 using (/) to divide it into a float so that it is printed in euro and cent amount as shown in (2).
3. According to (3) and (4), f or f-strings means formatted string literals, which is a new string formatting approach in Python 3.6 and above. it is not a function. I also noticed spacing between prompt and result, so (\n) was applied.
4. The program was then tested using other amounts and consistently displayed the correct sum.

### Conclusion:
This output was achieved from the bank.py program:
Enter amount1(in cent): 65
Enter amount2(in cent): 180

The sum of these is €2.45

The same output with the correct sum can be derived when different amounts are entered at prompts, eg:
Enter amount1(in cent): 53
Enter amount2(in cent): 173

The sum of these is €2.26

### References:
1. https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/
2. https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
3. https://realpython.com/python-string-formatting/
4. https://realpython.com/python-f-strings/


## **WEEK 3 TASK: accounts.py** 

### Task 3 Description: 
*Bank account numbers can be stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs). This task is to write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).* 

*$ python accounts.py*

*Please enter an 10 digit account number: 1234567890*

*XXXXXX7890*

*Extra:
To modify the program to deal with account numbers of any length (a vague requirement, comment my assumptions)*

### Method:
1. First, I defined and prompted the 10 digit account number. Remember that the account number is a string.
2. For the first method in Question 1, I sliced the string to replace the first 6 numbers with X and display only the last 4 digits of the account number following (1) and (2). The replacement is defined as "XXXXXX" and the syntax used is replace(old, new, count), where old=digits I want to replace, new=what I want to replace it with, and count=how many times I want to perform the replacements. I set it to 1, so it won't replace anything but the first occurrence of the substring.
3. For the second method in Question 1, the length function, len() was used for this program as shown in (3) and (4). First I defined and prompted for  the account number. I then sliced the string into 2, which were replacement and display. Because a string is a list, replacement=length(all-4) multiplied by "X" which is a string, becomes N(X). This means that all of the numbers but the last 4 were replaced by "X". I displayed only the last 4 of the input string and printed out an output of replacement+display.
4. The account number length is unknown in Question 2. The length function, len(), is again used for this program as shown in (3) and (4). First I defined and prompted for account number of any length. I then sliced the string into 2, which were replacement and display. Because a string is a list, replacement=length(all-4) multiplied by "X" which is a string, becomes N(X). This means that all of the numbers but the last 4 were replaced by "X". I displayed only the last 4 of the input string and printed out an output of replacement+display.

### Conclusions:
1. This output was achieved using 2 different programs, the first uses replace function and the second uses replace and length functions:
Please enter an 10 digit account number: 1234567890
XXXXXX7890
2. For an account number with unknown length which displays only the last 4 digits and replaces the others with X, this output was achieved using replace and length functions:
Please enter your account number: 99887766554433221100
XXXXXXXXXXXXXXXX1100
3. Different account number lengths could be due to:
- different banks
- the date when the account was opened, ie. older accounts are shorter, newer accounts are longer
- the country where the account was opened, eg: Ireland uses IBAN, USA uses ABA routing transit numbers, Malaysia uses SWIFT code.
- branch code/sort code
- routing codes
The use of this program is not only limited to banks, but other consumers which requires bank account numbers, such as money transfer websites which is used globally. So the program should be able to accommodate any account length from banks around the world, which can be up to 34 characters.
So I assumed that input_string is the account number of ANY length. Hence, to display only the last 4 digits, I used (len(input_string) MINUS 4) MULTIPLIED BY X. So all these other front digits will be displayed as X.

### References:
1. https://www.w3schools.com/python/python_strings_slicing.asp
2. https://dirask.com/posts/Python-replace-first-3-characters-in-string-j8g65p
3. https://www.w3schools.com/python/ref_func_len.asp
4. https://stackoverflow.com/questions/49701989/python-replace-character-range-in-a-string-with-new-string

## **WEEK 4 TASK: collatz.py**

### Task 4 Description: 
*This task is to write a python program called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.  
At each step, to calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Also, to have the program end if the current value is one.*

*Example of it running:*

*$ python collatz.py*

*Please enter a positive integer: 10*

*10 5 16 8 4 2 1*   *(notice the spaces between the numbers, use builtin, maybe separator sep="", end="" )*

### Method:
1. I created a prompt to enter a positive integer as an integer.
2. The numbers were determined to be in a list as shown in (1).
3. The output will contain a list of appended numbers (2).
4. I used a While loop which will end when the value is 1, and assigned temp_posint as temporary storage because I have to declare a variable somewhere.
5. If...Else was used (3) because it only has odd or even numbers. If the number is even, divide by 2 in integer form (4) and if odd, multiply by 3 and add 1, again in integer form.
6. The next subsequent numbers will be replaced by temp_posint, because it is a whole sequence of numbers.
7. Finally the sequence of numbers was printed out with space between the numbers using separator sep=" " according to (5) and (6).

### Conclusion:
Two programs were written to get the output. However, the first resulted in the numbers displayed in square brackets []. Program 2 resulted in the desired output using separator.

### References:
1. https://www.w3schools.com/python/python_lists.asp
2. https://realpython.com/python-append/
3. https://www.w3schools.com/python/python_conditions.asp
4. https://www.w3schools.com/python/python_numbers.asp
5. https://www.geeksforgeeks.org/python-sep-parameter-print/
6. http://anh.cs.luc.edu/170/mynotes/sepend.html


## **WEEK 5 TASK: weekday.py** 

### Task 5 Description:
*The task is to write a program that outputs whether or not today is a weekday. The program should be called weekday.py, where I will need to search the web to find how I work out what day it is. An example of running this program on a Thursday is given below.*

$ python weekday.py

Yes, unfortunately today is a weekday.


*An example of running it on a Saturday is as follows:*

$ python weekday.py

It is the weekend, yay!


### Method:
1. I searched (1) to find out how to work out what day it is and decided to use module datetime (2).
2. First, I imported the datetime module. Then, I defined day of the week by inserting the module, class, argument and function (isoweekday) as shown in (3) and (4). In isoweekday, numbers 1 to 5 are designated to Monday to Friday, while Saturday is 6 and Sunday is 7.
3. I used conditions If, else (5) because it only involved 2 situation: weekday or weekend. If the numbers are <6, then it would output "Yes, unfortunately today is a weekday. Or else, it would output "It is the weekend, yay!".

### Conclusion:
The program outputs "Yes, unfortunately today is a weekday." from Monday to Friday and "It is the weekend, yay!" on the weekends.

### References:
1. https://pynative.com/python-get-the-day-of-week/  
2. https://docs.python.org/3/library/datetime.html#module-datetime
3. https://pythontic.com/datetime/datetime/isoweekday
4. https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday
5. https://www.w3schools.com/python/python_conditions.asp

## **WEEK 6 TASK: squareroot.py** 

### Task 6 Description:
*The task is to write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
*I am to create a function called <tt>sqrt</tt> that does this. I was asked to create my own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). The newton method at estimating square roots was suggested.*

$ python squareroot.py

Please enter a positive number: 14.5

The square root of 14.5 is approx. 3.8.

 
### Method:
1. I researched square root approximation using the Newton method (1-5) and decided to use (5) because it is simple and elegant.
2. First, I created a prompt to enter a prompt that will take in a float.
3. Then I created a function with one argument (flonum) according to (6) to follow the formula newtsqrt = 0.5*(guess+(flonum/guess)), where I let flonum to be be any number, and guess is the approximation of the square root of flonum. I also declared the variables in the formula.
4. I used the While loop (7) to get the guess and better approximations of the square root and returned the final number rounded up to 1 decimal point (8).
5. Finally I called the function to print out the number and its square root as shown in (6).

### Conclusion:
The program outputs the square root approximation of a positive floating-point number using the Newton Method.

### References:
1. https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
2. https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
3. https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method
4. https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
5. https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx
6. https://www.w3schools.com/python/python_functions.asp
7. https://www.w3schools.com/python/python_while_loops.asp
8. https://www.w3schools.com/python/ref_func_round.asp

## **WEEK 7 TASK: es.py** 

### Task 7 Description:
*The task is to write a program that reads in a text file and outputs the number of e's it contains. It requires one to think about what is being asked here and document any assumptions one makes. The program should take the filename from an argument on the command line.*

$ python es.py moby-dick.txt

116960

### Method:
1. I downloaded the Moby Dick text file from Project Gutenberg (1).
2. To take the filename from an argument on the command line, I used argparse according to (2) and (3) by importing the argparse module, instantiating an argumentParse class instance, called the argument "FILENAME", and then parse the argument.
3. Then, I accessed the FILENAME argument and opened the read only file (4) and decided to start my e_counter from "CHAPTER 1" and end before the sentence "End of this Project Gutenberg etext of Moby Dick, by Herman Melville'" using the string split method (5).
4. I set the e_counter at 0 and used the For Loop (6). I converted the whole text into capital letters to get all the Es and not distinguish between small and capital letters from the original text.
5. I added 1 in the amount to account for the E in CHAPTER 1 and printed the final answer.
6. Note: The number of 'e' from moby-dick.txt retrieved from this program is less than task instruction because it discounted texts before CHAPTER 1 and the last statement declared by the online publisher.

### Conclusion:
This program outputs the number of E in the moby-dick.txt file using the argparse module. The number of 'e' from moby-dick.txt retrieved from this program is less than task instruction because it discounted texts before Chapter 1 and the last statement declared by the online publisher.

### References:
1. https://www.gutenberg.org/files/2701/old/moby10b.txt
2. https://docs.python.org/3/library/argparse.html
3. https://realpython.com/command-line-interfaces-python-argparse/
4. https://www.w3schools.com/python/python_file_open.asp
5. https://www.w3schools.com/python/ref_string_split.asp
6. https://www.w3schools.com/python/python_for_loops.asp

## **WEEK 8 TASK: plottask.py** 

### Task 8 Description:
*The task is to write a program called plottask.py that displays:*

*1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2*

*2. and a plot of the function  h(x)=x3 in the range [0, 10],* 

*on the one set of axes.*

*Some marks will be given for making the plot look nice (legend etc).*


### Method:
1. Looking at the question, I decided that it would be overlay plots (1,2).

### Conclusion:


### References:
1. https://stackoverflow.com/questions/67253174/how-to-set-space-between-the-axis-and-the-label/67253601
2. https://kaleidoscopicdiaries.wordpress.com/2015/05/30/distance-between-axes-label-and-axes-in-matplotlib/
3.
