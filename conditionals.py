# If/ Else conditions are used to decide to do something based on something being true or false

x = 50
y = 49 + 1


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')


# Logical operators (and, or, not) - Used to combine conditional statements

z = 4
h = 5

# in and opertator both have to be treu to run 
if z > 2 and z <=10:
    print(f'{z} is greater than 2 ans less than 10')

# in or, one has to be true to run
if h > 9 or h >= 4:
    print(f'{h} is less than 9 but greater than 4 ')

# not 
if not(h == z):
    print(f'{h} is not equal to {z}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

g = 100
number = [1,2,3,4,5,6,7,8,9]

# in 
if g in number:
    print(g in number)

# not in 
if g not in number:
    print(g not in number)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

q = 8
f = 8

if q is f:
    print(q is f)

if q is not f:
    print(q is not f)