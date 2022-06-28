# Description:
#
#         Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.
#
#         If it does, print True. Else, print False.
#
#         This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
#
#         If the length of the suffix is greater than the length of the string, print False.

s = 'Heloo'
prefix = 'loo'
prefix2 = 'looo'
prefix3 = 'Heloooo'
print(s.endswith(prefix))
print(s.endswith(prefix2))
print(s.endswith(prefix3))

#option2

s = 'Heloo'
prefix = 'loo'
if s[len(s)-len(prefix)::] == prefix:
    print(True)
else:
    print(False)

