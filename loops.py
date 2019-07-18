 # A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Kamal', 'ali', 'heba', 'sara']

# for loop
# for person in people:
#     print(f'Current Person: {person}')

# Break 
# for person in people:
# 	if person == 'heba':
# 		break
# 	print(f'Current Person: {person}')

# Continue 
for person in people:
	if person == 'heba': 
		continue # this will skip over heba and continue the loop 
	print(f'current person: {person}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
	print(f'count: {count}')
	count += 1
