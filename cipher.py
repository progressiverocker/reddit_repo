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
            list_of_request = []
            for letters in user_request.strip():
                list_of_request.append(letters.lower())
            return list_of_request        
        else:
            print ("\n\tOops! Please try again.")


def generate_cypher(list_of_request):
    list_of_ascii = []
    
    for letters in string.ascii_lowercase:
        list_of_ascii.append(letters)
        
    cypher_range = randrange(1,26)
    list_of_ascii_sliced = list_of_ascii[:cypher_range]
    list_of_ascii_cypher = list_of_ascii[cypher_range:]
    
    for letters in list_of_ascii_sliced:
        list_of_ascii_cypher.append(letters)

    for request_index, letter_request in enumerate(list_of_request):
        for ascii_letter in list_of_ascii:
            if letter_request == ascii_letter:
                list_of_request[request_index] = list_of_ascii_cypher[list_of_ascii.index(ascii_letter)]

    print cypher_range    
    print "\nHere is your cypher: ", ''.join(list_of_request)


restart = 'y'
while restart == 'y':
    generate_cypher(request_cypher())
    restart = raw_input("\nRestart type 'Y'.").lower().strip()

    


