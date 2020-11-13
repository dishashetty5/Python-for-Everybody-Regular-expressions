# Python-for-Everybody-Regular-expressions
Regular expressions(Chapter 11)

Regular expressions are almost their own little programming language for searching
and parsing strings. As a matter of fact, entire books have been written on the
topic of regular expressions. In this chapter, we will only cover the basics of regular
expressions. For more detail on regular expressions, see:
https://en.wikipedia.org/wiki/Regular_expression
https://docs.python.org/library/re.html


11.9 Exercises

Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^Xmbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
