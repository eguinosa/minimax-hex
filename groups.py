# Gelin Eguinosa Rosique

import tourney
from group import connected_group

# # Testing the Code:
# from game_logic import Game


class Groups:
    """
    Class to control all the different groups of stones on the map for one player.
    """

    def __init__(self, game, player):
        """
        Search the map for all the stones of the player and organize them in groups,
        where all the stones in a group are connected.
        """
        self.game = game
        self.player = player
        self.groups = self.__search_groups()
        self.length = self.__length()

    def __search_groups(self):
        """Looks in the map to form the groups of the stones the player has."""
        groups = []
        search_map = [[False] * tourney.SIZE for _ in range(tourney.SIZE)]
        # Flag to continue looking for groups in the map:
        continue_search = True
        while continue_search:
            group_found, result_group = connected_group(self.game, self.player, search_map)
            if group_found:
                groups.append(result_group)
            else:
                continue_search = False
        return groups

    def __length(self):
        if self.groups:
            max_group = max(self.groups, key=lambda x: x.length)
            max_length = max_group.length
            return max_length
        # No groups found:
        return 0


# if __name__ == '__main__':
#     game4 = Game(4)
#     game4.board[1][0] = 'B'
#     game4.board[0][1] = 'B'
#     game4.board[3][0] = 'B'
#     game4.board[2][1] = 'B'
#     game4.board[1][2] = 'B'
#     game4.board[0][3] = 'B'
#     game4.board[3][2] = 'B'
#     game4.board[2][3] = 'B'
#     game4.board[3][3] = 'B'
#
#     the_groups = Groups(game4, 'W')
#     print(the_groups.groups)
#     print(the_groups.length)


