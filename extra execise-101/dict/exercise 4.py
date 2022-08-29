# Description:
#
# Write a Python program that checks if all values in a dictionary are equal.
# If they are, print True. Else, print False.
# If the dictionary is empty, print "Empty".

my_dict1 = {"a": 1, "b": 2, "c": 3}
values = my_dict1.values()
print(set(values))
if len(set(values)) == 1:
    print(True)
elif len(set(values)) == 0:
    print('emoty')
else:
    print(False)









