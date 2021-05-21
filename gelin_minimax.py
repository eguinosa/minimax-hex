# Gelin Eguinosa Rosique
# C-511

from tools import oo
from gelin_groups import Groups
from gelin_moves import moves


def alpha_beta(game, player, depth):
    """Return the best move for the player."""
    best_move, value = max_play(game, None, player, depth, -oo, oo)
    return best_move


def max_play(game, move, player, depth, alpha, beta):
    """Return the best move for the current player"""
    best_move = None
    max_value = -oo

    # Terminal states for the player:
    if game.winner() != '.':
        return move, 1 if game.winner() == player else -1
    if depth == 0:
        return move, heuristic(game, player)

    # Going through all the possible moves:
    for x, y in moves(game, player):
        _, value = min_play(game.clone_play(x, y), (x, y), player, depth - 1, alpha, beta)
        if value > max_value:
            best_move = (x, y)
            max_value = value
            alpha = max(alpha, max_value)
        if max_value >= beta:
            return best_move, max_value

    return best_move, max_value


def min_play(game, move, player, depth, alpha, beta):
    """Return the best move for the opposite player"""
    best_move = None
    min_value = oo

    # Terminal states for the player:
    if game.winner() != '.':
        return move, -1 if game.winner() == player else 1
    if depth == 0:
        return move, heuristic(game, player)

    # Going through all the possible moves:
    for x, y in moves(game, player):
        _, value = max_play(game.clone_play(x, y), (x, y), player, depth - 1, alpha, beta)
        if value < min_value:
            best_move = (x, y)
            min_value = value
            beta = min(beta, min_value)
        if min_value <= alpha:
            return best_move, min_value

    return best_move, min_value


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
