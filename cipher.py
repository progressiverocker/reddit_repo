'''
A program that can encrypt texts with an alphabetical caesar cipher.
This cipher can ignore numbers, symbols, and whitespace.
'''

import string # ascii_lowercase
from random import randrange

def request_cypher():
    # force input and keep looping until valid
    while True:
        user_request = raw_input("\nEnter your string: ")
        if user_request.strip() != "":
            # convert string into list
            request = list(user_request.strip().lower())
            return request         
        else:
            print ("\n\tOops! Please try again.")


def generate_cypher(request):
    ascii = list(string.ascii_lowercase)
    cypher_range = randrange(1,26)
    ascii_sliced = ascii[:cypher_range]
    ascii_cypher = ascii[cypher_range:]
    
    for letters in ascii_sliced:
        ascii_cypher.append(letters)

    for request_index, letter_request in enumerate(request):
        for ascii_letter in ascii:
            if letter_request == ascii_letter:
                request[request_index] = ascii_cypher[ascii.index(ascii_letter)]
    
    print "\nHere is your cypher: ", ''.join(request)


restart = 'y'
while restart == 'y':
    generate_cypher(request_cypher())
    restart = raw_input("\nRestart type 'Y'.").lower().strip()

    


