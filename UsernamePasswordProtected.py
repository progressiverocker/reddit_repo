#!py2.7

'''
A program which is password protected and won't open unless the correct user and password is given.
Have the user and password in a seperate .txt file. Break into your own program.
'''

import string
import random
from random import randrange
import re
FILENAME = r"output.txt"


# randomly generate a username and password in FILENAME
def login():
    username = ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase
                      + string.digits) for x in range(randrange(6,10)))
    password = ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase
                      + string.digits) for x in range(randrange(6,10)))
    
    with open(FILENAME, "w") as login:
        data = login.write("%s %s" %(username, password))


# force input for username and password
# loop until correct match on username and password
def prompt():
    accounts = {}
    
    while True:

        with open(FILENAME) as search:
            r = search.read()
            username, password = r.split() 
            accounts[username] = password
        enter_username = raw_input("\nEnter your username: ").strip()
        enter_password = raw_input("Enter your password: ").strip()

        if (enter_username != "") and (enter_password != ""):
            
            if enter_username in accounts and enter_password == accounts[username]:
                print "\n\tLogin Successful!"
                break                
            else:
                print "\n\tIncorrect Username or Password"
        
        else:
            print "\n\tOops! Please try again"



login()
prompt()

raw_input("\nLoading your program ...<Press Enter>")




