#Dictionary
# Dictionary is a mutable data type in Python.
# NOT indexable.
# A python dictionary is a collection of key and value pairs separated by a colon (:) & enclosed in curly braces {}.
# Keys must be unique in a dictionary, but duplicate values are allowed.

# Create Dictionary
mydict = dict() # empty dictionary
mydict = {} # empty dictionary
mydict = {1:'one' , 'A':'two' , 3:'three'} # dictionary with mixed keys
print(mydict)
print(mydict.keys()) # Return Dictionary Keys using keys() method
print(mydict.values()) # Return Dictionary Values using values() method
print(mydict.items()) # Access each key-value pair within a dictionary in a tuple.
# export of .items is a # view object. must be saved as list and tuple or tuple.
itemslist = list(mydict.items()) # items of dict saved as list and tuple, that contain tuple with keys and values.
print('itemslist:',itemslist)
itemslist = tuple(mydict.items()) # items of dict saved as tuple, that contain tuple with keys and values.
print('itemslist:',itemslist)
#mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']}

print('---------------------------------------')

# Create a dictionary from a sequence of keys (.fromkeys())
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
print(mydict3) # value of mydict3 updated, as List(value) is mutable

# above method can just create keys, seperately. whole value,[10,20,30], set as value for each key.
print('---------------------------------------')

# Create a dictionary from list and tuple or tuple.

# tuple or list and tuple members must be 'couple'.
tuple1 = (('name','ali'),('age',23))
newdict = dict(tuple1)
print(newdict)

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
print('\n')
dict1 = {4:'four'}
mydict.update(dict1) # update dict by update() method by add other dict1.
print(mydict.items())
mydict.pop(4) # Removing items(key:value) in the dictionary using Pop(key) method
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

print('---------------------------------------')

# Dictionary Comprehension
double = {i:i*2 for i in range(10)} #double each value using dict comprehension
print(double)

key = ['one' , 'two' , 'three' , 'four' , 'five']
value = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(key,value)} # using dict comprehension to create dict
print(mydict)
mydict1 = {'a':10 , 'b':20 , 'c':30 , 'd':40 , 'e':50}
mydict1 = {k:v/10 for (k,v) in mydict1.items()} # Divide all values in a dictionary
print(mydict1)

print('---------------------------------------')

# Word Frequency using List
mystr4 = "one two three four one two two three five five six seven six seven one"
mylist = mystr4.split() # Split String into substrings
print(type(mylist))
print(mylist)
mylist1 = set(mylist) # Unique values in a list and tuple
mylist1 = list(mylist1)
print(mylist1)

print('---------------------------------------')

# Calculate frequenct of each word is list and tuple
count1 = [0] * len(mylist1)
print(count1)
mydict5 = dict()
for i in range(len(mylist1)): # for on mylist1 that is a set and we don't have reputation.
    for j in range(len(mylist)): # for on original list and tuple with reputation.
        if mylist1[i] == mylist[j]:
            count1[i] += 1
    print(count1)
    mydict5[mylist1[i]] = count1[i]
print(mydict5)

# Calculate frequenct of each word is list and tuple ------- my code:
count2=0
count3=[]
mydict5 = dict()
mydict6 = dict()
for i in range(len(mylist1)): # for on mylist1 that is a set and we don't have reputation.
    for j in range(len(mylist)): # for on original list and tuple with reputation.
        if mylist1[i] == mylist[j]:
            count2 +=1
    count3.append(count2) # append to a list and tuple to save the count.
    count2 = 0
    mydict6[mylist1[i]] = count3[i]
print(mydict6)





