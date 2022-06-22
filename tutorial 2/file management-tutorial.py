# File Management
# Python has several built-in modules and functions for creating, reading, updating and deleting files.

# open file:
#fileobj = open('test1.txt') # Open file in read/text mode
#fileobj = open('test1.txt', 'r') # Open file in read mode
#fileobj = open('test1.txt', 'w') # Open file in write mode
#fileobj = open('test1.txt', 'a') # Open file in append mode

# close file:
#fileobj.close()

#********* read file:
fileobj = open('test1.txt')
a = fileobj.read() # method read(): Read whole file
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
print(fileobj.readline()) # method readline(): read every line cursor in it. Read first line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read second line of a file.
print(fileobj.tell()) # Get the file cursor position
print(fileobj.readline()) # Read third line of a file.

print('----------------')
print('***reaadlines***')
fileobj.seek(0)
a = fileobj.readlines() # method readlines(): Read all lines of a file and save into a list.
    ## the list is like the txt. can reach to every line by
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
print('# write with w and write)
fileobj = open("test2.txt", "w") # Create a new file
fileobj.write("First Line\n")
fileobj.write("Second Line\n")
fileobj.write("Third Line\n")
fileobj.write("Fourth Line\n")
fileobj.write("Fifth Line\n")
fileobj.close()
fileobj = open('test2.txt')
print(fileobj.readlines())














