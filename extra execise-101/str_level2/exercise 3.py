# Description:
#
#  Write a Python program that prints a copy of the string s without any spaces.
#
#  Words should be connected in the final string.
#
#  If the string doesn't contain spaces, print it intact.

s = 'hello,        world'
print(s)

new_s = ''
for char in s:
    if char != ' ':
        new_s += char
    else:
        continue
print(new_s)


#option #2

s = s.replace(' ','')

print(s)


#option #3

s= '   hello, world salam    '
print(s)
a = s.split()
print(a)
new_s = ''
for i in a:
    new_s += i
print(new_s)
























