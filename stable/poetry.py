# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:16:59 2017

This function uses a predefined dictionary to generate a poem from a template.
It's very deep and a little bit edgy.

@author: robert-karl
"""

def ChooseWord(choices,Nword,posLabel,posVocab):
    """
    Chooses a word of a given part of speech, then removes that word from the dictionary.
    Inputs:
        choices     The dict of selected words
        Nword       The number of words of that part of speech to take
        posLabel    Label for tis part of speech
        posVocab    The array of words for that part of speech
    Returns:
        choices     The updated dict of selected words
    """
    from random import choice
    for word in range(0,Nword):
        # Pick a word
        newWord = choice(posVocab)
        # Add the word to the choices dict
        choices[posLabel+str(word)]=newWord
        # Remove the word so that it will not be selected twice
        posVocab.remove(newWord)
    return choices

def makePoem():
    # Poetic structure
    structure = "{art0} {adj0} {noun0} \n\n{art0} {adj0} {noun0} {verb0} {pre0} the {adj1} {noun1}\n{adv0}, the {noun0} {verb1} the {noun1} \n{verb1} {pre1} {art1} {adj2} {noun2}."
    
    # Build the vocabulary
    adjectives = ['furry','balding','incredulous','fragrant','exuberant','glistening','hopeful']
    nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']
    verbs = ['kicks','jingles','bounces','slurps','meows','explodes','curdles']
    adverbs = ['curiously','extravagantly','tantalizingly','furiously','sensuously']
    prepositions = ['against','after','into','beneath','upon','for','in','like','over','within']
    
    # Select the words, put them in the choices dictionary
    choices = {}
    # Select the words that we need
    Nadj = 3
    choices = ChooseWord(choices,Nadj,'adj',adjectives)
    Nn = 3
    choices = ChooseWord(choices,Nn,'noun',nouns)
    Nv = 2
    choices = ChooseWord(choices,Nv,'verb',verbs)
    Nadv = 1
    choices = ChooseWord(choices,Nadv,'adv',adverbs)
    Np = 2
    choices = ChooseWord(choices,Np,'pre',prepositions)
        
    # Set the articles based on the following word
    # These are the letters that force a preceeding artice to be an, not a
    vowels = 'aeiouh'
    if vowels.find(choices['adj0'][0])>=0:
        choices['art0'] = 'an'
    else:
        choices['art0'] = 'a'
    if vowels.find(choices['adj2'][0])>=0:
        choices['art1'] = 'an'
    else:
        choices['art1'] = 'a'
        
    # Build the poem
    poem = structure.format(**choices)

    # Capitalize the first letter
    poem = poem[0].upper()+poem[1:]
    
    return poem

print(makePoem())
exitString = 'Press <ENTER> to exit.'
input(exitString)