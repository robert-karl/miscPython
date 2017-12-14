# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:07:31 2017

This function takes a user input and turns it into L33T 5P34K

@author: rinfi_000
"""
print("Please type phrase to be translated: ")
phrase = input()

# Now we will replace various lower case letters
phrase = phrase.replace('a','4')
phrase = phrase.replace('e','3')
phrase = phrase.replace('o','0')
phrase = phrase.replace('l','1')
phrase = phrase.replace('s','5')
phrase = phrase.replace('t','7')
phrase = phrase.replace('b','8')

# output the final result
print(phrase)