# Description:
#  Write a Python Program that prints the reversed version of a string.
#  The program must preserve uppercase and lowercase letters.
#  If the string is empty, print it intact.

str = 'ali'
def reverse():
    a = input('enter a word to print reverse: ')
    newchar = ''
    for char in a[::-1]:
        newchar += char
    return newchar

print(reverse())

def reverse2(a):
    print(a[::-1])

reverse2('Hello')
