# Description:
#
#  Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.
#
#  If it does, print True. Else, print False.
#
#  This test should be case sensitive. For example, "A" should not be equivalent to "a".
#
#  If the length of the prefix is greater than the length of the string, print False.

s = 'Heloo'
prefix = 'he'
prefix2 = 'He'
prefix3 = 'Heloooo'
print(s.startswith(prefix))
print(s.startswith(prefix2))
print(s.startswith(prefix3))

#option2

s = 'Heloo'
prefix = 'he'
if s[:len(prefix)] == prefix:
    print(True)
else:
    print(False)