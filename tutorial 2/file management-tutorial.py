# File Management
# Python has several built-in modules and functions for creating, reading, updating and deleting files.

# open file:
#fileobj = open('test1.txt') # Open file in read/text mode
#fileobj = open('test1.txt', 'r') # Open file in read mode
#fileobj = open('test1.txt', 'w') # Open file in write mode
#fileobj = open('test1.txt', 'a') # Open file in append mode

# close file:
#fileobj.close()

# read file:
fileobj = open('test1.txt')
a = fileobj.read() #Read whole file
print(a)
print('----------------')
b= fileobj.read() #File cursor is already at the end of the file so it won't be able to read anything.
print(b) # ---------> print nothing

fileobj.seek(0) # Bring file cursor to initial position.

b= fileobj.read()
print(b)

print('----------------')

fileobj.seek(700) # place file cursor at loc 700
b= fileobj.read()
print(b)

print('----------------')

fileobj.seek(0)
a = fileobj.read(16) # Return the first 16 characters of the file
print(a)

print(fileobj.tell()) # Get the file cursor position

print('----------------')
print('***reaadline***')
fileobj.seek(0)
print(fileobj.readline()) # readline(): read every line cursor in it. Read first line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read second line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read third line of a file.

print('----------------')
print('***reaadlines***')
fileobj.seek(0)
a = fileobj.readlines() # readlines(): Read all lines of a file and save in a list.
print(a)
print(type(a))

# Read first 5 lines of a file using readline()
fileobj.seek(0)
count = 0
for i in range(5):



for i in range(5):
    if (count < 5):
        print(fileobj.readline())
 else:
    break
 count+=1














