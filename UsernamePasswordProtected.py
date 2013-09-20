'''
Your challenge for today is to create a program which is password protected,
and won't open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
For even more extra credit, break into your own program :)
'''

import string
import random
from random import randrange


def login():
    username = str(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(randrange(6,10))))
    password = str(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(randrange(6,10))))
    with open(r"Output.txt", "w") as login:
        data = login.write("%s\n%s" % (username, password))
        
login()


print 'Username:'
username = raw_input()
print 'Password:'
password = raw_input()

with open(r"Output.txt", "r") as login:
    if username and password in login.read().split():
        raw_input('Login Successful!')
    else:
        raw_input('Please Try Again!')
    
        

