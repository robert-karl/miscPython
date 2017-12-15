# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:59:56 2017

Here we take a string from the user, and perform a simple cypher on it. 
We change each letter of the alphabet to a different letter by shifting an integer amount.

Any numbers or other special characters will be left alone.
@author: robert-karl
"""

from string import ascii_lowercase as letters

Nlett = len(letters)
Nshift = 2 #The size of the shift for the cypher
request = "What would you like to encrypt?\n"
secret = input(request)
# This will store the encrypted message
revealed = ''
'''#First a way from a little googling
for char in secret:
    if char in letters:
        # append the shifted letter to the revealed message
        revealed += letters[(letters.index(char)+Nshift)%Nlett] 
    else:
        revealed += char
'''
# After more google, here is a faster way
lettersShift = letters[Nshift:]+letters[0:Nshift]
revealed = secret.translate(secret.maketrans(letters,lettersShift))
# Now to get the uppercase letters also
revealed = revealed.translate(revealed.maketrans(letters.upper(),lettersShift.upper()))

# display the message
print('{}\nbecomes\n{}'.format(secret,revealed))
# Let the user close when finished.
closing = 'Press <ENTER> to close.'
input(closing)