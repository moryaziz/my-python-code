# 📌 Description:
#
#         Write a Python program that prints a string reversed using a loop.
#
#         All the characters must be on the same line in reverse order.

mystr = 'hello'
length = len(mystr)
new_str =''
for i in mystr[-1::-1]:
        new_str += i
print(new_str)