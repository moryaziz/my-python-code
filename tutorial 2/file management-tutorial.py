# File Management
# Python has several built-in modules and functions for creating, reading, updating and deleting files.

# addressing:
# we have two way for give the address of a file to python:
# 1- absolute path:
# C:\users\......\github\sample.txt
# 2- relative path:
# get in place where the .py file is already stored.
# sample.txt:\.


# open file:
# we have two ways to open a file: 1- ordinary       2-pythonic

# ordinary:
# fid = open('sample.txt') ----------- in ordinary way , it should be closed.
# fid.close()

# pythonic:
# with open ('sample.txt') as fid:

# different mode of opening:
#fileobj = open('test1.txt') # Open file in read/text mode
#fileobj = open('test1.txt', 'r') # Open file in read mode
#fileobj = open('test1.txt', 'w') # Open file in write mode
#fileobj = open('test1.txt', 'a') # Open file in append mode

# close file:
#fileobj.close()

#********* read file:
# we have 3 way for reading the txt file:
# readline
# readlines
# read

# ***** read ***** : read file character by character, we can determine the number of characters e.g: read

fileobj = open('test1.txt')
a = fileobj.read() # method read(): Read whole file
print(a)
print('----------------')
b= fileobj.read() #File cursor is already at the end of the file so it won't be able to read anything.
print(b) # ---------> print nothing
print('nothing')

fileobj.seek(0) # Bring file cursor to initial position.

print('----------------')

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

# ***** readline *****: # read line by line and cursor go to beginning of next line.

# problem: if we have enter('\n') in the file, as the print method has end=\n it in by default,
# then we have two extra '\n'.
# solution : line = fid.readline().strip('\n')
print('***reaadline***')

fileobj.seek(0)
print(fileobj.readline()) # method readline(): read every line cursor in it. Read first line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read second line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read third line of a file.

print('----------------')

# ***** readlines *****:

print('***reaadlines***')
fileobj.seek(0)
a = fileobj.readlines() # method readlines(): Read all lines of a file and save into a list[] and tuple.
    ## the list and tuple is like the txt. can reach to every line by
print(a)
print('***************************')
print(a[1])
print('***************************')
print(type(a))

# Read first 5 lines of a file using readline()
fileobj.seek(0)
count = 0
for i in range(5):
    print(fileobj.readline())

print('----------------')

# Read first 5 lines of a file using readlines()
fileobj.seek(0)
count = 0
for i in fileobj.readlines():
    if count <= 5:
        print(i)
    else :
        break
    count += 1


print('-----------------------------------')

print('*****write file: ******')
# Write File :
    # open as 'a' :
fileobj = open('test1.txt', 'a')
fileobj.write('THIS IS THE NEW CONTENT APPENDED IN THE FILE') # Append content to
fileobj.close()
fileobj = open('test1.txt')
a = fileobj.readlines()
print(a[-1])

    # open as 'w' :
    ## if we run these codes, ALL data in test1.txt erased and replace with appended content.
# fileobj = open('test1.txt', 'w')
# fileobj.write('THIS IS THE NEW CONTENT APPENDED IN THE FILE') # Append content to file.
#fileobj.close()
#fileobj = open('test1.txt')
#a = fileobj.readlines()
#print(a[-1])

print('create a new file with \'w\' method: ')
print(' write with w and write')
fileobj = open("test2.txt", "w") # Create a new file
fileobj.write("First Line\n")
fileobj.write("Second Line\n")
fileobj.write("Third Line\n")
fileobj.write("Fourth Line\n")
fileobj.write("Fifth Line\n")
fileobj.close()
fileobj = open('test2.txt')
print(fileobj.readlines())

#
#
#
#
#
#







