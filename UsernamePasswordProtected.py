'''
A program which is password protected and won't open unless the correct user and password is given.
Have the user and password in a seperate .txt file. Break into your own program.
'''

import string
import random
from random import randrange

# generates random username and password. Stores in file.
def login():
    username = str(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(randrange(6,10))))
    password = str(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(randrange(6,10))))
    with open(r"Output.txt", "w") as login:
        data = login.write("%s\n%s" % (username, password))
        
login()

# prompt user and test username and password.
print 'Username:'
username = raw_input()
print 'Password:'
password = raw_input()

with open(r"Output.txt", "r") as login:
    if username and password in login.read().split():
        raw_input('Login Successful!')
    else:
        raw_input('Please Try Again!')
    
        

