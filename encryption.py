# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:59:56 2017

@author: rinfi_000
"""

from string import ascii_lowercase as letters

Nlett = len(letters)
Nshift = 2
secret = '''map'''
revealed = ''

#First a way from a littel googling
for char in secret:
    if char in letters:
        revealed += letters[(letters.index(char)+Nshift)%Nlett]
    else:
        revealed += char
    
print('{} becomes {}'.format(secret,revealed))

# After more google, here is a faster way
lettersShift = letters[Nshift:]+letters[0:Nshift]
revealed = secret.translate(secret.maketrans(letters,lettersShift))
print('{} becomes {}'.format(secret,revealed))