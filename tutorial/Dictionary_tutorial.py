#Dictionary
#Dictionary is a mutable data type in Python.
#A python dictionary is a collection of key and value pairs separated by a colon (:) & enclosed in curly braces {}.
# Keys must be unique in a dictionary, but duplicate values are allowed.

# Create Dictionary
mydict = dict() # empty dictionary
mydict = {} # empty dictionary
mydict = {1:'one' , 'A':'two' , 3:'three'} # dictionary with mixed keys
print(mydict)
print(mydict.keys()) # Return Dictionary Keys using keys() method
print(mydict.values()) # Return Dictionary Values using values() method
print(mydict.items()) # Access each key-value pair within a dictionary
mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']}

print('---------------------------------------')

keys = {'a' , 'b' , 'c' , 'd'}
mydict3 = dict.fromkeys(keys) # Create a dictionary from a sequence of keys
print(mydict3)
keys = {'a' , 'b' , 'c' , 'd'}
value = 10
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of key and value.
print(mydict3)

print('---------------------------------------')

keys = {'a' , 'b' , 'c' , 'd'}
value = [10,20,30]
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of
print(mydict3)
value.append(40)
print(mydict3) # value of mydict3, updated as List(value) is mutable

print('---------------------------------------')

# Accessing Items
mydict = {'A':'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict['A']) # Access item using key
print(mydict[2]) # Access item using key
print(mydict.get(2)) # Access item using get() method

print('---------------------------------------')

# Add, Remove & Change Items
print('# Add, Remove & Change Items')
mydict = {'A':'one' , 2:'two' , 3:'three'}
mydict['A'] = 'zero' # Changing Dictionary Items
mydict[1] = 'zero' # Changing Dictionary Items
 ## if key does not exist in dict, added key and value to dict.
print(mydict.items())
dict1 = {4:'four'}
mydict.update(dict1) # update dict by update() method by add other dict1.
print(mydict.items())
mydict.pop(4) # Removing items in the dictionary using Pop() method
print(mydict.items())
mydict.popitem() # A random item is removed
del[mydict[3]] # Removing item using del method
print(mydict.items())
mydict.clear() # Delete all items of the dictionary using clear method
del mydict # Delete the dictionary object

print('---------------------------------------')

# Copy Dictionary
print('# Copy Dictionary')
mydict = {1:'one', 2:'two'}
mydict1 = mydict # Create a new reference "mydict1"
print(id(mydict) , id(mydict1)) # The address of both mydict & mydict1 will be the same
mydict2 = mydict.copy() # Create a copy of the dictionary
print(id(mydict2))

mydict[2] = 'two-new' # changing mydict affect mydict1
print(mydict)
print(mydict1) # mydict1 will be also impacted as it is pointing to the same dictionary
print(mydict2)

print('---------------------------------------')

# Loop through a Dictionary
print('# Loop through a Dictionary')
mydict = {1:'one', 2:'two'}
for i in mydict1:
    print(i , ':' , mydict1[i]) # Key & value pair


# Dictionary Membership
mydict = {1:'one', 2:'two'}
print(1 in mydict) # Test if a key is in a dictionary or not.
    # Membership test can be only done for keys.












