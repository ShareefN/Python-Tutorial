# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

UserJSON = '{"name": "shareef", "gender":"male", "age":19}'

# parse to dictionary 
user = json.loads(UserJSON)
# print(user)

# Get name
# print(user['name'])

# Dictionary to JSON 

car = {'make': 'ford', 'modal': 'mustang', 'year':2012}

carJSON = json.dumps(car)
print(carJSON)