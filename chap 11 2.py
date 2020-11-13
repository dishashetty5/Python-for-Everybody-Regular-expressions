#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average as an integer.
#Enter file:mbox.txt
#38549
#Enter file:mbox-short.txt
#39756
import re
filename=input("enter the file name: ")
fhand=open(filename)
list=[]
for line in fhand:
    match=re.search("New\sRevision:\s(\d+)",line)
    if match:
        list.append(int(match.group(1)))
print(sum(list)//len(list))
