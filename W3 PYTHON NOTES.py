#

'''JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation. '''

'''ile handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.'''

#open demofile.txt
'''
f = open("C:\\Users\hp\Desktop\demofile.txt", "r")


#print(f.read())
#print(f.readline()) #reads 1 line at a time

#loop throught the line
for x in f:
    print(x)
'''


f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

