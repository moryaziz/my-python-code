# Description:
#
# Write a Python program that prints the largest of the values in a dictionary.
#
# You may assume that all the values in the dictionary are either lists or tuples.

sumof = 0
my_dict = {"a": [1, 2, 3],"b": [4, 0, -4],"c": [3, 5, 9],"d": [45, 12, 100]}
for i in my_dict.values():
    if sum(i) > sumof:
        sumof = sum(i)
    else:
        pass
print(sumof)








