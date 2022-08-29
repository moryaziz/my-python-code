# Description:
#
#         Write a Python program that checks if a key exists in a dictionary or not.
#         If the key exists in the dictionary, print True. Else, print False.
#         The key should be stored in the variable key.

mydict = {'a':2,'b':5}
def check_key(ke):
    if ke in mydict:
        print(True)
    else:
        print(False)

check_key('a')








