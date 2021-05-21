# Gelin Eguinosa Rosique
# C-511

from gelin_group import connected_group


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
        max_group, max_length = self.__max_length_group()
        self.max_group = max_group
        self.max_length = max_length

    def empty_neighbours(self):
        """
        Return the empty positions around the biggest group of stones
        in the board.
        """
        if self.max_group:
            result = self.max_group.empty_neighbours()
        else:  # self.max_group == None
            result = []
        return result

    def __search_groups(self):
        """Looks in the map to form the groups of the stones the player has."""
        groups = []
        search_map = [[False] * self.game.size for _ in range(self.game.size)]
        # Flag to continue looking for groups in the map:
        continue_search = True
        while continue_search:
            group_found, result_group = connected_group(self.game, self.player, search_map)
            if group_found:
                groups.append(result_group)
            else:
                continue_search = False
        return groups

    def __max_length_group(self):
        """
        Looks for the most expanded group of stones,
        and returns it with its length.
        """
        if self.groups:
            max_group = max(self.groups, key=lambda x: x.length)
            max_length = max_group.length
            return max_group, max_length
        # No groups found:
        return None, None
