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
    
    # Build the vocabulary
    adjectives = ['furry','balding','incredulous','fragrant','exuberant','glistening']
    nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']
    verbs = ['kicks','jingles','bounces','slurps','meows','explodes','curdles']
    adverbs = ['curiously','extravagantly','tantalizingly','furiously','sensuously']
    prepositions = ['against','after','into','beneath','upon','for','in','like','over','within']
    
    # Select the words, put them in the choices dictionary
    choices = {}
    # For the structure above we need
    
    # 3 adjectives
    Nadj = 3
    for adj in range(0,Nadj):
        newAdj = choice(adjectives)
        choices['adj'+str(adj)]=newAdj
        adjectives.remove(newAdj)
    
    # 3 nouns
    Nn = 3
    for nn in range(0,Nn):
        newNoun = choice(nouns)
        choices['noun'+str(nn)]=newNoun
        nouns.remove(newNoun)
    
    # 2 verbs
    Nv = 2
    for vv in range(0,Nv):
        newVerb = choice(verbs)
        choices['verb'+str(vv)]=newVerb
        verbs.remove(newVerb)
    
    # 1 adverb
    Nadv = 1
    for adv in range(0,Nadv):
        newAdv = choice(adverbs)
        choices['adv'+str(adv)]=newAdv
        adverbs.remove(newAdv)
    
    # 2 prepositions
    Np = 2
    for pp in range(0,Np):
        newPrep = choice(prepositions)
        choices['pre'+str(pp)]=newPrep
        prepositions.remove(newPrep)
        
    # Set the articles based on the following word
    vowels = 'aeiou'
    if vowels.find(choices['adj0'])>=0:
        choices['art0'] = 'an'
    else:
        choices['art0'] = 'a'
    if vowels.find(choices['adj2'])>=0:
        choices['art1'] = 'an'
    else:
        choices['art1'] = 'a'
        
    # Build the poem
    poem = structure.format(**choices)

    # Capitalize the first letter
    poem = poem[0].upper()+poem[1:]
    
    return poem

print(makePoem())