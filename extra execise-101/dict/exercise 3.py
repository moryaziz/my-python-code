# Description:
#
# Write a Python program that merges two dictionaries and prints the resulting dictionary.
#
# "Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries.

my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

my_dict1.update(my_dict2)
print(my_dict1)


