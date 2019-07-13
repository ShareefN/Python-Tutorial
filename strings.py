# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Shareef'
age = 19

# concatinating
# print('Hello my name is ' + name + ', I am ' + str(age) + ' years old.')

# String Formatting

# Arguments by position 
# print('Hello my name is {name}, I am {age}'.format(name='Ali', age='12'))

# F-string
# print(f'Hello my name is {name}, I am {age} years old.')

# String Methods

s = 'hello world'
# capitalize string 
print(s.capitalize())
print(len(s)) # length of string
print(s.replace('world', 'everything')) # replaces words
print(s.split()) # splits the word into an array
print(s.find('e')) # find the index of the letter