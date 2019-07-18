# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayHello(name):
  print(f'Hello {name}')

sayHello('shareef')

# Return values 
def getSum(n1, n2):
  total = n1 + n2
  return total

result = getSum(13, 5)
# print(result)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# def lambda 
getTotal = lambda n1, n2: n1 + n2

total = getTotal(1, 10)
print(total)