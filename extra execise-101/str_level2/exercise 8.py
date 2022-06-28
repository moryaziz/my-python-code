# Description:
#
# write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order,
# and print the resulting string.
#
#  You may assume that the string only contains letters and spaces to separate the words.
#
#  Spaces should be preserved in the final string.

s = 'HEllo world'
low_s = s.lower()
s_list = low_s.split()
new_s =''
for word in s_list:
    for char in sorted(word):
        new_s += char
    new_s += ' '
print(new_s)
sort = sorted(s_list)
print(sort)
a = 'acb'
q = sorted(a)
print(q)








