#Description:

# Write a Python program that prints the character at index i in the string s.

# If the index is out of range, the program should print "i is out of range"

# If the string is empty, the program should print "Empty String"

while True:
    a = input('enter a word to print the length, for quit type \'q\': ')
    b = int(input('insert index: '))
    a.lower()
    if b > len(a):
        print('i is out of range')
    elif a[b-1] == ' ' :
        print('Empty String')
    else:
        print(a[b-1])

