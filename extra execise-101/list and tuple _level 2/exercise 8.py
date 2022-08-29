import itertools
# Description:
#
# Write a Python program that generates and prints all the possible permutations of a list.
# A permutation is a possible arrangement of the elements of the list.
# For example, [2, 1, 3] is a permutation of [1, 2, 3].
# Print each permutation as a list on a separate line. You can print them as lists or tuples.
# Include the list itself as a permutation.


mylist = []
mylist1 = []
list1 = [1,2,3]
for ifd in itertools.permutations(list1):
    print (ifd)



