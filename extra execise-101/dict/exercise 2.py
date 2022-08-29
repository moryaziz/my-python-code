# Description:
#
# Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.
# if the key-value pair exists in the dictionary, do not update the existing value.
# The dictionary should not be modified in this case.
# Store the new key in the new_key variable and the new value in the new_value variable.
# Print the final value of the dictionary.

mydict ={"January": 45, "February": 56, "March": 67}
def add_key_value(dict,key,value):
    if not key in dict:
        dict[key] = value
    else:
        pass

add_key_value(mydict,"March",66)
print(mydict)











