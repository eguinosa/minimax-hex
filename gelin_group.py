# Gelin Eguinosa Rosique

class Group:
    """Class to represent a group of stone with the same color"""

    def __init__(self, positions, game, player):
        """
        Save the location of the stones of the group, the board and the player.
        Look how many rows or columns covers, to see how close to winning is the
        player.
        """
        self.positions = positions
        self.game = game
        self.player = player
        min_pos, max_pos, group_length = self.__length()
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.length = group_length

    def __length(self):
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
            return y_min, y_max, y_length

        # self.player == 'B'
        x_min = min(self.positions, key=lambda pos: pos[0])
        x_max = max(self.positions, key=lambda pos: pos[0])
        x_length = x_max[0] - x_min[0] + 1
        return x_min, x_max, x_length


def connected_group(game, player, visited_area):
    """Search for all the connected stones of the same player"""
    positions = []
    neighbours = []
    # Flag to stop the double for
    stop = False
    for x in range(game.size):
        for y in range(game.size):
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
    result_group = Group(positions, game, player)
    return found_group, result_group
