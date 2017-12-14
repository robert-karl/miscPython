# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:19:02 2017

This program runs tic-tac-toe between two players.

@author: rinfi_000
"""
import numpy as np
from matplotlib import pyplot as plt

def setUp():
    '''This is the initialization where the player can choose settings'''
    print('Welcome to Tic-Tac-Toe')
    playerX = input('Who is playing as X?')
    playerO = input('Who is playing as O?')
    return (playerX,playerO)
def writeBoard(board):
    '''This function takes the current board state and displays it to the user.'''
    plt.imshow(board)

Nrow = 3
Ncol = 3
board = np.zeros([Ncol,Nrow])
writeBoard(board)
winnner = ''

pX,pO = setUp()
while winner=='':
    board = makeMove(board,currentPlayer)
    checkWin()
