# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:56:18 2020

@author: Casey

Just a general practice of dictionaries with a very poorly structured
representation of Tic Tac Toe.

Does not actually function to say any winners and allows for space
overwriting.
"""


theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '}


def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])
    
turn = 'X'
print('To claim a space, for rows enter top, mid, or low.Then either L, M, or R. Such as topL or midM.')
print('Does not actually check to see who wins and will allow for space overwriting.')
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Claim which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


printBoard(theBoard)
    