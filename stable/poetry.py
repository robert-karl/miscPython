# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:16:59 2017

This function uses a predefined dictionary to generate a poem from a template.
It's very deep and a little bit edgy.

@author: robert-karl
"""



def makePoem():
    from random import choice

    # Poetic structure
    structure = "{art0} {adj0} {noun0} \n\n{art0} {adj0} {noun0} {verb0} {pre0} the {adj1} {noun1}\n{adv0}, the {noun0} {verb1} the {noun1} \n{verb1} {pre1} {art1} {adj2} {noun2}."
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
    poem = structure.format(adj0=adjChoice[0],adj1=adjChoice[1],adj2=adjChoice[2],noun0=nChoice[0],noun1=nChoice[1],noun2=nChoice[2],verb0=vChoice[0],verb1=vChoice[1],adv0=advChoice[0],pre0=pChoice[0],pre1=pChoice[1],art0=art[0],art1=art[1])
    ''' Here's a key to what the numbers are:
        0,1,2       adjectives
        3,4,5       nouns
        6,7         verbs
        8           adverbs
        9,10        prepositions
        11,12       articles
    '''
    # Capitalize the first letter
    poem = poem[0].upper()+poem[1:]
    
    return poem

print(makePoem())