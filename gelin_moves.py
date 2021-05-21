# Gelin Eguinosa Rosique
# C-511

from math import sqrt
from gelin_groups import Groups


def moves(game, player):
    """
    Return a list of all the empty positions sorted by the
    convenience of the move.
    """
    player_groups = Groups(game, player)
    group_moves = player_groups.empty_neighbours()
    empty_moves = empty_pos(game)
    for x, y in group_moves:
        yield x, y
    for x, y in empty_moves:
        if (x, y) in group_moves:
            continue
        yield x, y


def empty_pos(game):
    """
    Return the list of empty positions in the board, sorted by how close
    they are to the center.
    """
    result_pos = []
    for x in range(game.size):
        for y in range(game.size):
            if game[x, y] == '.':
                result_pos.append((x, y))
    # Sort the positions depending on how close they are to the middle
    result_pos.sort(key=lambda pos: distance_to_middle(pos, game.size))
    return result_pos


def distance_to_middle(pos, size):
    """Return how far is the given position from the middle of the board."""
    x = pos[0]
    y = pos[1]
    middle_x = (size - 1) / 2
    middle_y = middle_x
    dist = sqrt((middle_x - x) ** 2 + (middle_y - y) ** 2)
    return dist
