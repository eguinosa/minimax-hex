# Gelin Eguinosa Rosique

class Group:
    """Class to represent a group of stone with the same color"""

    def __init__(self, game, player, positions):
        """
        Save the location of the stones of the group, the board and the player.
        Look how many rows or columns covers, to see how close to winning is the
        player.
        """
        self.positions = positions
        self.game = game
        self.player = player
        # Checking the length of the group
        min_pos, max_pos, group_length = self.__length()
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.length = group_length

    def on_min_edge(self):
        """Determine if the player has reach the minimum edge of the board"""
        if self.player == 'W':
            y = self.min_pos[1]
            result = y == 0
        else:  # self.payer == 'B'
            x = self.min_pos[0]
            result = x == 0
        return result

    def on_max_edge(self):
        """Determine if the player has reach the maximum edge of the board"""
        if self.player == 'W':
            y = self.min_pos[1]
            top_edge = self.game.size - 1
            result = y == top_edge
        else:  # self.player == 'B'
            x = self.min_pos[0]
            top_edge = self.game.size - 1
            result = x == top_edge
        return result

    def empty_neighbours(self):
        """Look for all the empty cells that are next to the stones of the group"""
        result_neighbours = []
        search_map = [[False] * self.game.size for _ in range(self.game.size)]
        for position in self.positions:
            x = position[0]
            y = position[1]
            search_map[x][y] = True
            for nx, ny in self.game.neighbour(x, y):
                if search_map[nx][ny]:
                    continue
                search_map[nx][ny] = True
                if self.game[nx, ny] == '.':
                    result_neighbours.append((nx, ny))
        # Sort the neighbours depending on how much they get closer the player to the edges
        result_neighbours.sort(key=lambda pos: self.__pos_advantage(pos))
        return result_neighbours

    def __pos_advantage(self, pos):
        """
        Gives a value determining how good would it be to play in this position of the board
        for the player.
        -1: if it expands the group one step
        0: if it is in the edge of the group
        positive number: if it is inside the edges of the group
        """
        if self.player == 'W':
            y = pos[1]
            min_y = self.min_pos[1]
            max_y = self.max_pos[1]
            if y < min_y or y > max_y:
                return -1
            if y == min_y or y == max_y:
                return 0
            distance_to_edge = max(y-min_y, max_y - y)
            return distance_to_edge
        # self.player == 'B'
        x = pos[0]
        min_x = self.min_pos[0]
        max_x = self.max_pos[0]
        if x < min_x or x > max_x:
            return -1
        if x == min_x or x == max_x:
            return 0
        distance_to_edge = max(x - min_x, max_x - x)
        return distance_to_edge


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
    result_group = Group(game, player, positions)
    return found_group, result_group
