# Player Template
# IMPORTANT:    This module must have a function called play
#               that receives a game and return a tuple of
#               two integers who represent a valid move on
#               the game.
from math import sqrt

from game_logic import *
from minimax import minimax

from gelin_groups import Groups

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

    return minimax(game, player, 3, heuristic, moves)


def moves(game, player):
    """
    Return a list of all the empty positions sorted by the
    convenience of the move.
    """
    player_groups = Groups(game, player)
    group_moves = player_groups.empty_neighbours()
    group_moves = group_moves[:6] if len(group_moves) > 6 else group_moves
    empty_moves = empty_pos(game, player)
    for x, y in group_moves:
        yield x, y
    for x, y in empty_moves:
        if (x, y) in group_moves:
            continue
        yield x, y


def empty_pos(game, player):
    """
    Return the list of empty positions in the board, sorted by how close
    they are to the center.
    """
    result_pos = []
    for x in range(game.size):
        for y in range(game.size):
            if game[x, y] == EMPTY:
                result_pos.append((x, y))
    # Sort the positions depending on how close they are to the middle
    result_pos.sort(key=lambda pos: distance_to_middle(pos, game.size))
    return result_pos


def distance_to_middle(pos, size):
    x = pos[0]
    y = pos[1]
    middle_x = (size - 1) / 2
    middle_y = middle_x
    dist = sqrt((middle_x - x) ** 2 + (middle_y - y) ** 2)
    return dist


def heuristic(game, player):
    """
    Heuristic Based on how much distance from one side to the other
    the player has covered.
    - Min value: -1
    - Max value: 1
    """
    enemy = 'B' if player == 'W' else 'W'
    player_groups = Groups(game, player)
    enemy_groups = Groups(game, enemy)
    # Divides the difference between the two players by the game.size to keep
    # the result between -1 and 1.
    result = (player_groups.max_length - enemy_groups.max_length) / game.size
    return result
