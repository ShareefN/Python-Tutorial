# A List is a collection which is ordered and changeable. Allows dupl icate members.

# Creating lists 
number = [1, 2, 4, 5, 7]
fruits = ['apple', 'orange', 'mango', 'banana']

# print(number)

# Get the value
print(fruits[3])

# Get the length 
print(len(fruits))

# Append to the end of th elist 
fruits.append('grapes')

#  Remove from the list 
fruits.remove('mango')

# Change the value of an element
fruits[2] = 'jelly'

# Insert to a specific position
fruits.insert(3, 'strawbwrries')

# Remove from specific position 
fruits.pop(4)

# Reverse the list 
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort list (will sort the list in the oposite direction)
fruits.sort(reverse = True)

print(fruits)