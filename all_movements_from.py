# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 02:03:15 2018

@author: luisxavierramostormo


TWO PLAYER GAME CRACKER
-Positions in game are defined by list of ints (length is degrees of freedom)
    -Must be immutable
"""



def all_movements_from(position, player):
    """
    Generator of all possible positions reachable from the current position by
    the specified player
    Inputs:
        player (int): 0 or 1
        position: current position of the game
    returns:
        generator of all possible positions
    """
    yield from all_movements_from_tick_tack_toe(position, player)
    
def all_movements_from_tick_tack_toe(position, player):
    """
    Implementation of all_movements_from specific to tick tack toe
    """
    for i in range(3):
        for j in range(3):
            if position[i][j] not in (0, 1):
                movement = [[position[row][col] for col in range(3)] for row in range(3)]
                movement[i][j] = player
                yield tuple(tuple(movement[row]) for row in range(3))


    
