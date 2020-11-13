#Exercise 1: Write a simple program to simulate the operation of the
#grep command on Unix. Ask the user to enter a regular expression and
#count the number of lines that matched the regular expression:
#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author
#$ python grep.py
#Enter a regular expression: ^Xmbox.txt had 14368 lines that matched ^X-
#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$
import re
filename=input("enter the file name: ")
regex=input("enter the regular expression: ")
count=0
fhand=open(filename)
for line in fhand:
    line=line.rstrip()
    if re.search(regex,line):
        count=count+1
print(count)
