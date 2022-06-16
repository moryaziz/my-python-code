# Operators
# Operators are special symbols in Python which are used to perform operations on variables/values.


# Arithmetic Operators
a = 5
b = 2
x = 'Asif'
y = 'Bhat'

# Addition
c = a + b
print('Addition of {} and {} will give :- {}\n'.format(a,b,c))

#Concatenate string using plus operator
z = x+y
print ('Concatenate string \'x\' and \'y\' using \'+\' operaotr :- {}\n'.format(z))

# Subtraction
c = a - b
print('Subtracting {} from {} will give :- {}\n'.format(b,a,c))

# Multiplication
c = a * b
print('Multiplying {} and {} will give :- {}\n'.format(a,b,c))

# Division
c = a / b
print('Dividing {} by {} will give :- {}\n'.format(a,b,c))

# Modulo of both number
c = a % b
print('Modulo of {} , {} will give :- {}\n'.format(a,b,c))
# Power

c = a ** b
print('{} raised to the power {} will give :- {}\n'.format(a,b,c))
# Division(floor)

c = a // b
print('Floor division of {} by {} will give :- {}\n'.format(a,b,c))

print('-------------------------------')

# Comparison Operators
# Comparison operators are used to compare values.

x = 20
y = 30
print('Is x greater than y :- ',x>y) #----False
print('\nIs x less than y :- ',x<y) #----True
print('\nIs x equal to y :- ',x==y) #----False
print('\nIs x not equal to y :- ',x!=y) #----True
print('\nIs x greater than or equal to y :- ',x>=y) #----False
print('\nIs x less than or equal to y :- ',x<=y) #----True

a = 'Asif'
b = 'Bhat'
c = 'Asif'
print(a == b , a ==c , a != b) # Comparison operators on string

print('-------------------------------')

# Logical Operators
x = True
y = False
print('Logical AND operation :- ',x and y) # True if both values are true
print('Logical OR operation :- ',x or y) # True if either of the values is true
print('NOT operation :- ',not x ) # True if operand is false

print('-------------------------------')

# Assignment Operators

x = 10
print('Initialize x with value 10 (x=10)) :- ',x)
x+=20 # x = x+20
print ('Add 20 to x :- ',x)
x-=20 # x = x-20
print ('subtract 20 from x :- ',x)
x/=10 # x = x/10
print ('Divide x by 10 :- ',x)
x*=10 # x = x*10
print ('Multiply x by 10 :- ',x)
x = int(x)
x**=2 # x = x**2
print ('x raised to the power 2 :- ',x)
x%=2
print ('Modulo Division :- ',x)
x = 20
x//=3
print ('Floor Division :- ',x)

print('-------------------------------')

# Membership Operators
    #Membership Operators are used to test whether a value / variable is present in a sequence.

mystr = 'ali bahar'
print('ali' in mystr)
print('bah' in mystr) # return true however part of word,exist.




