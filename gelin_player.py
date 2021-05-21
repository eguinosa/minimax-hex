# Player Template
# IMPORTANT:    This module must have a function called play
#               that receives a game and return a tuple of
#               two integers who represent a valid move on
#               the game.
# from math import sqrt
# from game_logic import *

# from minimax import minimax
# from gelin_minimax import heuristic

from gelin_minimax import alpha_beta

# game_logic
#
#   EMPTY
#   PLAYER[0]
#   PLAYER[1]

# game
#   -> current (W or B)
#       It refers to the player who must play in
#       this turn.
#   -> indexing
#       game[i,j] return the player who have played
#       on position <i;j> (compare with PLAYER[0]
#       and PLAYER[1]). EMPTY if none player have
#       played there.
#   -> neighbour
#       creates an iterator that yields all
#       coordinates <x;y> who are neighbour of
#       current coordinates.
#
#       for nx, ny in game.neighbour(x, y):
#           print(nx, ny)


def play(game, player):
    # Code Here
    # Random player implementation (just delete it)
    # return minimax(game, player, 3, heuristic, moves)
    return alpha_beta(game, player, 3)
