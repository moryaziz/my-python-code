# flow control:
# if , elif, else:
# the following problem is called "chained conditioning" problem.
# where running of the conditions are related to each other condition.
# tradition way:
print('***chained conditioning:***')
age =50
if age > 35:
    print('old')
elif age >= 18 and age <= 35 :
    print('young')
else:
    print('child')

print('***unchained conditioning:***')
# where running of  conditions are not related to each other condition and each condition is checked at the same time.

age = 50
if age > 35:
    print('old')
if age >= 18  :
    print('young')
# the way that upper code is right are a tradition way.
# when the condition have a right(non-zero) amount, the condition is True.

# false condition : int = 0 , float = 0.0, list and tuple = [], dict = {},strings =''
# the modern way :
age = 18
if age: # age have a amount so = True.
    print('')
if not age-18 : # if not = false.
    print('age is 18')
age = 19
if not age-18 : # condition for checking age == 18
    print('age is 18') # doesn't print anything.

# ternary operator:
vote = True if age >18 else False # write conditions in one statement.
print(vote)


# loops:

# ********* for *********:

# iterable object: something that can be iterated to every element of it.
# like: list and tuple, string, range

for i in range(3):
    print(i)
# i is iterator. range is iterable object.
# in : for checking subset and being member.
# break : stop loop and exit from loop.
# continue : go next iterator object without run.
print('\n')

alphabet = 'ABCDEFGHIJKLMNOPQR'
for char in alphabet:
    if char in 'FIR':
        break
    if  char in 'BCD':
        continue
    else:
        print(char)
        
# enumurate: get iterator object and devote counter to it.
# have counter and iterator as same time.
alphabet1 = 'ABCDEF'
for ind,char in enumerate(alphabet1):
    print('{}:{}'.format(ind,char))

print('\n')

# zip: allow using two iterator and iterable object in one loop:
numbers = '1234'
character = "abcdef"
for num,char in zip (numbers,character):
    print('{}:{}'.format(num,char))

# ******** while *********:
# while <condittion>:
# but usually we write : 'while True': and use 'break' inside while body.


























