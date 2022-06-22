# Description:

# Write a Python program that prints the first and last three characters of the string s as a single string.

# If the string has less than six characters, print an empty string (blank output).

str1= 'hellloo'
#print(str1[:3]+(str1[-1:-4:-1])[::-1]  )

def first_last(str):
    f = int(input('number of first and last: '))
    l = len(str)
    if len(str) < f*2 :
        print('')
    else:
        first = str[:f]
        last = str[-1:-1-f:-1]
        last_reverse = last[::-1]
        return first+last_reverse

def first_last2(str):
    f = int(input('number of first and last: '))
    l = len(str)
    if len(str) < f*2 :
        print('')
    else:
        first = str[:f]
        last = str[l-3:]
        return first+last

print(first_last2('helllloppo'))






















