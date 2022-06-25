# Description:
#
#  Write a Python program that prints a copy of the string s without any spaces.
#
#  Words should be connected in the final string.
#
#  If the string doesn't contain spaces, print it intact.

s = 'hello        world'
for char in s:
    new_s = ''
    if char != ' ':
        new_s += char
    else:
        continue


print(s)
print(s.strip())
print(s.rstrip())


