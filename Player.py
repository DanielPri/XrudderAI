from TileColor import TileColor


class Player:

    def __init__(self, board, name, color):
        self.board = board
        self.name = name
        self.color = color
        self.played_pieces = []

    def play_turn(self):
        played = False
        token_selected = False

        if len(self.played_pieces) == 0:
            choice = 1
        else:
            choice = self.select_action()

        if choice is 1:
            while not played:
                position = (input(self.name + " select a position to place your token: ")).upper().replace(" ", "")
                tile = self.select_tile(position)
                if tile is None:
                    continue
                if self.play_tile(tile):
                    self.played_pieces.append(position)
                    played = True
        elif choice is 2:
            while not token_selected:
                position = (input(self.name + " select a token on the board: ")).upper().replace(" ", "")
                tile = self.select_tile(position)
                if tile is None:
                    continue
                if tile.get_color().value is not self.color.value:
                    print("You do not have a token at this position")
                    continue
                else:
                    token_selected = True
            while not played:
                new_position = (input("Choose a location to move token at position [" + position + "]: ")).upper()\
                    .replace(" ", "")
                new_tile = self.select_tile(new_position)
                if new_tile is None:
                    continue

                if self.play_tile(new_tile):
                    tile.set_color(TileColor.BLANK)
                    self.played_pieces.remove(position)
                    self.played_pieces.append(new_position)
                    played = True
        self.board.draw()

    @staticmethod
    def select_action():
        while 1 is 1:
            print("Choose an action")
            print("1. Place a token")
            print("2. Move a token")
            try:
                choice = int(input())
            except ValueError:
                print("Please enter a number")
                continue
            if choice != 1 and choice != 2:
                print("Please enter a valid number")
                continue
            return choice

    def select_tile(self, position):
        if position[0].isalpha() and position[1:].isdigit():
            if self.board.is_valid_position(position[0], position[1:]):
                return self.board.get_tile(position[0], position[1:])
            else:
                print("Please enter a valid tile")
                return None
        else:
            print("Please enter a valid input")
            return None

    def play_tile(self, tile):
        if tile.get_color().value is not TileColor.BLANK.value:
            print("That position is already occupied!")
            return False
        else:
            tile.set_color(self.color)
            return True
