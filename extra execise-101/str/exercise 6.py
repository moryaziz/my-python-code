# description:
#
# Write a Python program that prints the string s without the character at index n.
#
# if the index n is out of range, print the string s intact.
#
# If the string s is empty, print the string s intact.


def remove_index(str,i):
    new_str = ''
    l = len(str)
    for char in str:
        if i > l :
            return str
            break
        elif char == str[i]:
            continue
        else: #char != str[i]:
            new_str += char
    return new_str

print(remove_index('hello',3))




















