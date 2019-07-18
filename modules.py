# A module is basically a file containing a set of functions to include in your application. There are core python modules, 
# modules you can install using the pip package manager (including Django) as well as custom modules

# importing modules 
import datetime
from datetime import date
from time import time

# today = datetime.date.today()
today = date.today()
timeStamp = time()

# print(timeStamp)

# import pip module 
import camelcase
from camelcase import CamelCase

c = CamelCase()

# print(c.hump('hello world'))

# import custom module
from validator import validate_email

email = 'shareefyahoo.com'
if validate_email(email):
    print('Email Is Valid')
else: 
    print('Invalid Email')