# Player Template
# IMPORTANT:    This module must have a function called play
#               that receives a game and return a tuple of
#               two integers who represent a valid move on
#               the game.

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

# Gelin Eguinosa Rosique
# C-511

from gelin_minimax import alpha_beta


def play(game, player):
    """
    Calls the alpha-beta method to find the best
    possible move for the player.
    """
    return alpha_beta(game, player, 3)
