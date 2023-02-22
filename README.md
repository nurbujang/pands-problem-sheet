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

### Conclusion:
1. This output was achieved using 2 different programs, the first uses replace function and the second uses replace and length functions:
Please enter an 10 digit account number: 1234567890
XXXXXX7890
2. For an account number with unknown length which displays only the last 4 digits and replaces the others with X, this output was achieved using replace and length functions:
Please enter your account number: 99887766554433221100
XXXXXXXXXXXXXXXX1100
3. I assume that different account number lengths could be due to:
- different banks
- the date when the account was opened, ie. older accounts are shorter, newer accounts are longer
- the country where the account was opened, eg: Ireland uses IBAN, USA uses ABA routing transit numbers, Malaysia uses SWIFT code.
- branch code/sort code
- routing codes
The use of this program is not only limited to banks, but other consumers which requires bank account numbers, such as money transfer websites which is used globally. So the program should be able to accommodate any account length from banks around the world, which can be up to 34 characters.

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
1. I created a prompt to enter a positive integer as an integer
2. The numbers were determined to be in a list as shown in (1).
3. The output will contain a list of appended numbers (2).
4. I used a while loop which will end when the value is 1, and assigned temp_posint as temporary storage because we have to declare a variable somewhere.
5. If...Else was used (3) because it only has odd or even numbers. If the number is even, divide by 2 in integer form (4) and if odd, multiply by 3 and add 1 in integer form.
6. The next number will be replaced by temp_posint, because it is a whole sequence of numbers.
7. Finally the sequence of numbers was printed out with space between the numbers using forseparator sep=" " according to (5) and (6).

### Conclusion:
Two programs were written to get the output. However, the first resulted in the numbers displayed in square brackets []. Program 2 resulted in the desired output.

### References:
1. https://www.w3schools.com/python/python_lists.asp
2. https://realpython.com/python-append/
3. https://www.w3schools.com/python/python_conditions.asp
4. https://www.w3schools.com/python/python_numbers.asp
5. https://www.geeksforgeeks.org/python-sep-parameter-print/
6. http://anh.cs.luc.edu/170/mynotes/sepend.html


## **WEEK 5 TASK: .py** 

### Task 5 Description:
* *
* *

### Method:


### Conclusion:


### References:
1.
2.
3.

## **WEEK 6 TASK: .py** 

### Task 6 Description:
* *
* * 
* 
### Method:


### Conclusion:


### References:
1.
2.
3.

## **WEEK 7 TASK: .py** 

### Task 7 Description:
* *
* * 

### Method:


### Conclusion:


### References:
1.
2.
3.

## **WEEK 8 TASK: .py** 

### Task 8 Description:
* *
* * 

### Method:


### Conclusion:


### References:
1.
2.
3.
