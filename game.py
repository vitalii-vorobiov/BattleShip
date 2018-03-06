class Game:
    def __init__(self, fields, players, current_player):
        self.__fields = fields
        self.__players = players
        self.current_player = current_player

    def shoot_at(self, index, coordinates):
        """
        (index, tuple) -> (bool)

        """
        pass

    def field_with_ships(self, index):
        """
        (index) -> (str)

        """
        pass

    def field_without_ships(self, index):
        """
        (index) -> (str)

        """
        pass


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        """
        () -> (tuple)

        """
        pass


class Field:
    def __init__(self, ships):
        self.__ships = ships

    def shoot_at(self, coordinates):
        """
        (tuple) -> (bool)

        """
        pass

    def field_with_ships(self):
        """
        () -> (str)

        """
        pass

    def field_without_ships(self):
        """
        () -> (str)

        """
        pass


class Ship:
    def __init__(self, bow, horizontal, length, hit):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = hit

    def shoot_at(self, coordinates):
        """
        (tuple) -> (bool)

        """
        pass