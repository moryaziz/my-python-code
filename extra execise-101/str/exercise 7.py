# Description:
#
#         Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
#
#         curr_char and new_char are variables that contain strings with a single character.
#
#         You may assume that new_char will not be an empty string.
#
#         The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
#
#         If no match is found, print the initial string.


char2 = 'hello'
def change_word(curr_char,new_char):
    global char2
    a = char2.replace(curr_char,new_char)
    return a


#print(change_word('h','w'))

def change_word2(char,curr_char,new_char):
    a = char.replace(curr_char , new_char)
    return a


#print(change_word2('hello' , 'h' , 'w'))



char = input('input char: ')
curr_char = input('input curr_char: ')
new_char = input('input new_char: ')

print(change_word(curr_char , new_char))
print(change_word2(char, curr_char , new_char))
print(char.replace(curr_char , new_char))