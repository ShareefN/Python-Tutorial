# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary 

person = {
    'first_name': 'Shareef',
    'last_name': 'Nuseibeh',
    'age': 19
}

# Get value 
# print(person['first_name'],  person['last_name'])

# Add key/value 
person['phone'] = '555-555-555'

# print(person)

 # Get dict keys 
# print(person.keys())

# Get dict items
# print(person.items())

# Copy dict 
person2 = person.copy()
person2['city'] = 'Amman'

# print(person2)

# Remove item
del(person['age'])

# print(person)

# List of dic 
people = [
    {'name': 'Ali', 'Age': 23},
    {'name': 'Hassan', 'Age': 20}
]

print(people[0]['Age'])