import random

print(random.randrange(1, 10))  # 10 niet inbegrepen

# randint Return a number between 3 and 9 (both included):

import random
print(random.randint(3, 9)) # 3 en 9 inclusief

# Return a random element from a list:

import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) 

# Return random number between 0.0 and 1.0:

import random
print(random.random()) #float number between 0 and 1 

import random
print(random.uniform(20,60))
