# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 02:03:15 2018

@author: luisxavierramostormo


TWO PLAYER GAME CRACKER
-Positions in game are defined by list of ints (length is degrees of freedom)
    -Must be immutable
"""

from all_movements_from import all_movements_from
from victory import victory

    
def best_movement(current_position, player): # player is about to move
    """
    Builds game position tree from current state, and goes backwards to assign
    a score to each possible movement
    
    NEEDS MEMOIZATION
    """
    # if game is over, there's no movements to make
    if victory(current_position) != -1:
        print("game is over")
        return None
    
    # otherwise, check all movements
    score_dict = {} # memoization dict. Maps (position_by_player, player) -> score
    draw = None
    for movement in all_movements_from(current_position, player):
        # this new movement cannot be in the dictionary
        result, new_score_dict = score(movement, player, score_dict)
        score_dict = {**score_dict, **new_score_dict}
        if result == 1:
            print("you can win with this movement")
            return movement
        if result == .5:
            draw = movement
    if draw:
        print("you can't win, but at least you can force a draw with this movement")
        return draw
    print("you can't guarantee winning or even drawing")
    return None

def score(player_movement, player, score_dict = {}): 
    # if player makes his movement (and leaves board like this)
    """
    If other player plays next movement randomly, it returns the probability
    of winning.
    1 means we know we'll win with the right movements
    0 means other player can play so that he wins
    .5 means player left board so that no matter what the other player does,
     a draw can be forced
    (returns tuple. First val for x, second for o)
    
    COMPLETE!!!
    WORKING. TESTED
    
    NEEDS MEMOIZATION
    """
    # check if someone won with movement that just got made, or no more movements
    # can be made and it was a draw (base case for recursion)
    winner = victory(player_movement)
    if winner == player:
        score_dict[(player_movement, player)] = 1
        return 1, score_dict
    if winner == 1-player:
        score_dict[(player_movement, player)] = 0
        return 0, score_dict
    if winner == .5: #draw
        score_dict[(player_movement, player)] = .5
        return .5, score_dict
        
    # otherwise winner = -1, which means game is not over
    try: # try to use memoization dict
        return score_dict[(player_movement, player)], score_dict
    except KeyError:
        pass
    
    out = 1 # suppose our movement forces a win
    for next_position in all_movements_from(player_movement, 1-player): # all movements that the other player could make
        try:
            next_score = score_dict[(next_position, 1-player)]
        except KeyError:
            next_score, next_score_dict = score(next_position, 1-player)
            score_dict = {**score_dict, **next_score_dict}
        if next_score == 1:
            # if other player can make a movement that ensures that he wins
            return 0, score_dict # means our movement was bad
        if next_score == .5: # means other player can't win, but can force a draw
            out = .5 # means if other player can't win, at least he can force draw
    return out, score_dict
    
position = ((1, None, 1), (1, 0, 0), (0, 1, 1))
player = 1
print(best_movement(position, player))


    
