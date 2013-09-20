'''
A program that can encrypt texts with an alphabetical caesar cipher.
This cipher can ignore numbers, symbols, and whitespace.
'''

import string # ascii_lowercase
from random import randrange

def request():
    # force input and keep looping until valid
    while True:
        user_request = raw_input("\nEnter your string: ")
        if user_request.strip() != "":
            # convert string into list
            request = list(user_request.strip().lower())
            return request         
        else:
            print ("\n\tOops! Please try again.")


def encode(request):
    # use random number to encode request from user and print cipher
    ascii = list(string.ascii_lowercase)
    cipher_range = randrange(26)
    ascii_cipher = ascii[cipher_range:] + ascii[:cipher_range]
    char_encode = dict(zip(ascii, ascii_cipher))

    for index, key in enumerate(request):
        if key in char_encode:
            request[index] = char_encode[key]
    print "\nHere is your cipher: ", ''.join(request)


def decode(request):
    # produces 26 outcomes to solve the cipher
    # solutions provided by /u/SmartViking
    ascii = list(string.ascii_lowercase)
    raw_input("There are 26 possible solutions <Enter>")
    print "\n\tDecoded"
    rotations = [ascii[x:] + ascii[:x] for x in range(26)]
    count = 0
    for r in rotations:
        count += 1
        char_decode = dict(zip(r, ascii))
        decode = [char_decode.get(char, char) for char in request]
        print count, '\t', ''.join(decode)            

def restart():       
    restart = 'y'
    while restart == 'y':
        print ("\nWould you like to (e)ncode or (d)ecode a cipher?")
        pref = raw_input()
        if pref == pref.strip() != "":
            if pref.lower() == "e":
                encode(request())
            elif pref.lower() == "d":
                decode(request())
            else:
                print ("\n\tOops! Please select 'e' or 'd'")
        else:
            print ("\n\tOops! You need to enter something")

        restart = raw_input("\nRestart type 'Y'.").lower().strip()

print "A program that can encrypt texts with an alphabetical caesar cipher."
print "This cipher will ignore numbers, symbols, and whitespace."
restart()

    


