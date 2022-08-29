# Description:
#
# Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).
# The dictionary should only include the characters in the string.
# The test should be case-insensitive ("A" should be counted as "a").
# The keys in the dictionary should be lowercase letters.
# Only include letters in the dictionary.

mystr = "Hello, World"
mylist = []
for i in mystr:
    if i.isalpha():
        mylist.append(i.lower())

print(mylist)
count = 0
mydict = {}
for char in mylist:
    count = mylist.count(char)
    mydict[char] = count
print(mydict)









