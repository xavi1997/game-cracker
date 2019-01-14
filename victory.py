# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 02:03:15 2018

@author: luisxavierramostormo


TWO PLAYER GAME CRACKER
-Positions in game are defined by list of ints (length is degrees of freedom)
    -Must be immutable
"""

def victory(position):
    """
    Given a position in the game, indicates which player has won the game, or if
    the game ended in a draw, or if the game has not ended
    Inputs:
        position:
    Returns:
        0 (winner is 0)
        1 (winner is 1
        .5 (draw)
        -1 (no one has won but game hasn't ended)
    """
    return victory_tick_tack_toe(position)



def victory_tick_tack_toe(position):
    """
    Implementation of victory specific to tick tack toe
    """
    for i in range(3):
        if position[i][0] == position[i][1] == position[i][2]:
            return position[i][0]
    for i in range(3):
        if position[0][i] == position[1][i] == position[2][i]:
            return position[0][i]
    if position[0][0] == position[1][1] == position[2][2]:
        return position[0][0]
    if position[2][0] == position[1][1] == position[0][2]:
        return position[1][1]
    
    for i in range(3):
        for j in range(3):
            if position[i][j] not in (0, 1):
                return -1
    return .5

    
