# Description:
#
#  Write a Python program that reverses the individual words in the string s and changes their capitalization.
#  Uppercase letters should be printed in lowercase and vice versa.
#
#  Assume that the string only contains letters and spaces are used to separate words.

s= 'Hello World'
a = s.split()
new_s = ''
for char in a :
    for i in char[::-1]:
        new_s += i
    new_s += ' '
print(new_s)