# Gelin Eguinosa Rosique

import tourney

# Testing the Code:
from game_logic import Game

class Group:
    """Class to represent a group of stone with the same color"""

    def __init__(self, positions, game, player):
        """Save the location of the stones of the group, the board and the player."""
        self.positions = positions
        self.game = game
        self.player = player

    def length(self):
        """
        Look for how many of the rows ('B' player) or columns ('A' player) does this group
        covers, so to know how close is the player to win the game. If the player has
        covered all the rows or columns in a connected group, the player wins the game.
        :return: the number of columns or rows the group covers.
        """
        if self.player == 'W':
            y_min = min(self.positions, key=lambda pos: pos[1])
            y_max = max(self.positions, key=lambda pos: pos[1])
            y_length = y_max[1] - y_min[1] + 1
            return y_length

        # self.player == 'B'
        x_min = min(self.positions, key=lambda pos: pos[0])
        x_max = max(self.positions, key=lambda pos: pos[0])
        x_length = x_max[0] - x_min[0] + 1
        return x_length


def connected_group(game, player, visited_area):
    """Search for all the connected stones of the same player"""
    positions = []
    neighbours = []
    # Flag to stop the double for
    stop = False
    for x in range(tourney.SIZE):
        for y in range(tourney.SIZE):
            if visited_area[x][y]:
                continue
            elif game[x, y] != player:
                visited_area[x][y] = True
                continue
            else:
                # game[x, y] == player and not visited_area[x][y]:
                visited_area[x][y] = True
                positions.append((x, y))
                neighbours += list(game.neighbour(x, y))
                stop = True
            if stop:
                break
        if stop:
            break

    # No player found on the board
    if not positions:
        found_group = False
        return found_group, None

    # Search for all the positions of the player connected to the one in group
    while neighbours:
        x, y = neighbours.pop(0)
        if visited_area[x][y]:
            continue
        elif game[x, y] != player:
            visited_area[x][y] = True
            continue
        # game[x, y] == player and not visited_area[x][y]:
        visited_area[x][y] = True
        positions.append((x, y))
        neighbours += list(game.neighbour(x, y))

    found_group = True
    group = Group(positions, game, player)
    return found_group, group


if __name__ == '__main__':
    game4 = Game(4)
    game4.board[2][0] = 'W'
    game4.board[2][1] = 'W'
    game4.board[1][2] = 'W'
    game4.board[0][3] = 'W'
    game4.board[2][3] = 'W'
    player = 'W'
    vis_area = [[False] * 4 for _ in range(4)]
    result, group = connected_group(game4, player, vis_area)
    print(result)
    length = group.length()
    print(length)

