# Description:
#  Write a Python program that prints the string s without the characters located at even indices.
#
#  If the string is empty or only has one character, print it intact.

def even(str):
    if len(str)<2:
        return str
    else:
        return str[1::2]
print(even('coding'))














