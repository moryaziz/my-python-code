# Description:
#
# Write a Python program to count the number of repeated characters in the string s.
#
# The program must print the total number of repeated
# characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.
#
# If there are no repeated characters in the string, print 0 as the total count and None on the next line.

z = {}
s = 'helloo worllddd'
for i in s:
    if s.count(i) > 1 :
        z[i] = s.count(i)
        #z{i:a}
print(z)







