# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:16:59 2017

@author: rinfi_000
"""
from random import random

Ne = 10000 #number of elections to simulate

odds = [0.87,0.65,0.17,0.5]
Nr = len(odds)
victory=0
tie=0
for ee in range(0,Ne):
    wins=0
    for rr in range(0,Nr):
        if random()<=odds[rr]:
            wins+=1
    if wins>Nr/2:
        victory+=1
    if wins==Nr/2:
        tie+=1
oddsVic = victory/Ne
print("The odds of victory are {}".format(oddsVic))
oddsTie = tie/Ne
print("The odds of a tie are {}".format(oddsTie))
print("The odds of a loss are {}".format(1-oddsVic-oddsTie))