# Description:
#
#         Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a consonant. For example: "<char> is a <consonant | vowel>"
#
#         If the character is a special character, number, or symbol, print "<char> is not a letter".
#
#         If the string is empty, print "Empty String".

def check_sound2(stringg):
    list_vowel = ['o','u','i','a','e']
    list_letter = [':', ' ']
    for i in stringg:
        if i.isalpha():
            if i in list_vowel:
                print('{} is a vowel'.format(i))
            else:
                print('{} is a consonant'.format(i))
        elif i.isnumeric():
            print('{} is not a letter'.format(i))
        # elif i.isalpha():
        #     print('{} is a consonant'.format(i))
        else:
            print('{} is not a letter'.format(i))

check_sound2('score: 36')










