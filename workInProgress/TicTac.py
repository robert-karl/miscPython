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
def makeMove(board,player,name):
    valid = 0
    while valid==0:
        print("It's {}'s turn".format(name))
        locationY = int(input('Where will you play? Row:'))
        locationX = int(input('Column:'))
        if board[locationY,locationX]!=-1:
            print('Not valid, pick another spot.')
        else:
            board[locationY,locationX]=player
            valid=1
    return board
    
#def checkWin(board,cPlay):
#    '''Looks at the current board and determines if the current player just won.
#    Returns an empty string if the player has not won. Returns an integer 
#    denoting the current player if they have.'''
#    #v1 is completely manual for testing the rest of the program
#    win = input('Did the current Player win (y/n)?')
#    if win.lower()=='y':
#        return cPlay
#    else:
#        return ''
        
def checkWin(board,cPlay,Nwin):
    '''Looks at the current board and determines if the current player just won.
    Returns an empty string if the player has not won. Returns an integer 
    denoting the current player if they have.'''
    #v2 checks which squares are controlled by the current player and then sees 
    # if any row|column|diagonal is full
    
    controls = board==cPlay
    #Columns
    cols = np.sum(controls,0)
    testCols = cols==Nwin
    if np.sum(testCols)!=0:
        return cPlay
    #Rows
    rows = np.sum(controls,1)
    testRows = rows==Nwin
    if np.sum(testRows)!=0:
        return cPlay
    #Diagonals
    
    #If no victory is found, then no one has won yet
    return ''
        
def switchPlayer(cPlay):
    '''Takes the current player and switches to the other player.'''
    cPlay+=1
    cPlay=cPlay%2
    return cPlay
            

Nrow = 3
Ncol = 3
Nwin = 3 #The number of consecutive spaces needed in order to win
board = np.ones([Ncol,Nrow])*-1
writeBoard(board)
winner = ''
Nturn=0

playerNames = setUp()
#X goes first
currentPlayer = 0
while winner=='' and Nturn<Nrow*Ncol:
    board = makeMove(board,currentPlayer,playerNames[currentPlayer])
    writeBoard(board)
    winner = checkWin(board,currentPlayer,Nwin)
    Nturn+=1
    currentPlayer = switchPlayer(currentPlayer)

# State the winner
if winner=='':
    print('The game was a draw.')
else:
    print('The winner is {}!'.format(playerNames[winner]))