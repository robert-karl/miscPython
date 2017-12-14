# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:07:31 2017

This function takes a user input and turns it into L33T 5P34K
It does this by replacing lowercase letters with appropriate numerals

This is the assignment key:
o -> 0
l -> 1
NONE -> 2
e -> 3
a -> 4
s -> 5
NONE -> 6
t -> 7
b -> 8
NONE -> 9

@author: robert-karl
"""
import warnings


request = "Please type phrase to be translated: \n"
phrase = input(request)

# Assemble the key
oldChar = 'oleastb'
newChar = '0134578'

# Now we will replace various lower case letters
nConvert = min(len(oldChar),len(newChar))    # Avoids indexing out of range by only looping through the shorter string.
if len(oldChar)!=len(newChar):
    warnings.warn("The translation keys are of differrent lengths, not all letters have been translated.",RuntimeWarning)
for nn in range(0,nConvert):
    phrase = phrase.replace(oldChar[nn],newChar[nn])


# output the final result
print('\n')
print(phrase)
# Let the user determine when the program ends.
exitPrompt = 'Press <ENTER> to exit.'
input(exitPrompt)