from TileColor import TileColor

class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def play_turn(self, board):
        tile = None
        while tile is None:
            position = input(self.name + " select a position: ")
            if len(position) is 2 and position[0].isalpha() and position[1].isdigit():
                tile = board.get_tile(position[0], position[1])
                if tile.get_color().value is not TileColor.BLANK.value:
                    print("That position is already occupied!")
                    tile = None
            else:
                print("A position must be a letter followed by a number.")

        tile.set_color(self.color)
