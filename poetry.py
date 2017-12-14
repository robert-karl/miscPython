# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:16:59 2017

@author: rinfi_000
"""



def makePoem():
    from random import choice

    # Poetic structure
    structure = "{11} {0} {3} \n\n{11} {0} {3} {6} {9} the {1} {4}\n{8}, the {3} {7} the {4} \n{7} {10} {12} {2} {5}."
    """ Here's a key to what the numbers are:
        0,1,2       adjectives
        3,4,5       nouns
        6,7         verbs
        8           adverbs
        9,10        prepositions
        11,12       articles
    """
    
    # Build the vocabulary
    adjectives = ['furry','balding','incredulous','fragrant','exuberant','glistening']
    nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']
    verbs = ['kicks','jingles','bounces','slurps','meows','explodes','curdles']
    adverbs = ['curiously','extravagantly','tantalizingly','furiously','sensuously']
    prepositions = ['against','after','into','beneath','upon','for','in','like','over','within']
    
    # Select the words
    # For the structure above we need
    
    # 3 adjectives
    Nadj = 3
    adjChoice = []
    for adj in range(0,Nadj):
        newAdj = choice(adjectives)
        adjChoice.append(newAdj)
        adjectives.remove(newAdj)
    
    # 3 nouns
    Nn = 3
    nChoice = []
    for nn in range(0,Nn):
        newNoun = choice(nouns)
        nChoice.append(newNoun)
        nouns.remove(newNoun)
    
    # 2 verbs
    Nv = 2
    vChoice = []
    for vv in range(0,Nv):
        newVerb = choice(verbs)
        vChoice.append(newVerb)
        verbs.remove(newVerb)
    
    # 1 adverb
    Nadv = 1
    advChoice = []
    for adv in range(0,Nadv):
        newAdv = choice(adverbs)
        advChoice.append(newAdv)
        adverbs.remove(newAdv)
    
    # 2 prepositions
    Np = 2
    pChoice = []
    for pp in range(0,Np):
        newPrep = choice(prepositions)
        pChoice.append(newPrep)
        prepositions.remove(newPrep)
        
    # Set the articles based on the following word
    vowels = 'aeiou'
    art = ['a','a']
    if vowels.find(adjChoice[0][0])>=0:
        art[0] = 'an'
    if vowels.find(adjChoice[2][0])>=0:
        art[1] = 'an'
        
    # Build the poem
    poem = structure.format(adjChoice[0],adjChoice[1],adjChoice[2],nChoice[0],nChoice[1],nChoice[2],vChoice[0],vChoice[1],advChoice[0],pChoice[0],pChoice[1],art[0],art[1])
    ''' Here's a key to what the numbers are:
        0,1,2       adjectives
        3,4,5       nouns
        6,7         verbs
        8           adverbs
        9,10        prepositions
        11,12       articles
    '''
    poem = poem[0].upper()+poem[1:]
    
    return poem

print(makePoem())