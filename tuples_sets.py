# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 
# Creating tuples 
fruits = ('apple', 'oranges', 'banana')
fruits2 = ('apple')

# Get value
# print(fruits[0])

# Delete tuple 
# del fruits2
# print(fruits2)

# Get length of tuple 
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

vegitables = {'carrot', 'beans', 'tomato'}

# to check if elm is in set 
print('beans' in vegitables)

# To add to set 
vegitables.add('qugumber')
# print(vegitables)

# Remove from set 
vegitables.remove('beans')

# Clear set 
vegitables.clear()

# Delete set
# del vegitables

print(vegitables)
