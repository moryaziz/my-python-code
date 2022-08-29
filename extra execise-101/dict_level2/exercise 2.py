# 📌 Description:
#
#  Write a Python program that creates a dictionary from the values contained in nested lists.
# Each nested list has this format [value1, value2].
# value1 should be the key in the dictionary and value2 should be its corresponding value.
# there are no nested lists, print an empty dictionary.

nested = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
mydict = {}
for listac in nested:
    mydict[listac[0]] = listac[1]

print(mydict)






