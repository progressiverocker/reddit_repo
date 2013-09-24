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
        data = login.write("username: %s\npassword: %s" % (username, password))


# force input for username and password
# matches input from user with stored username and password in output.txt
# loop until correct match on username and password

def prompt():
    
    while True:
        search = open(r"Output.txt")
        username = [line for line in search if "username" in line]
        username = username[0].replace("username", '').strip()
        enter_username = raw_input("\nEnter your username: ").strip()
        
        search = open(r"Output.txt")
        password = [line for line in search if "password" in line]
        password = password[0].replace("password", '').strip()
        enter_password = raw_input("Enter your password: ").strip()

    
        if (enter_username != "") and (enter_password != ""):
            
            if (enter_username in username[0]) and (enter_password in password[0]):
                print "\n\tLogin Successful!"
                break
                
            else:
                print "\n\tIncorrect Username or Password"
        
        else:
            print "\n\tOops! Please try again"




login()
prompt()

raw_input("\nLoading your program ...<Press Enter>")

    
   
        

