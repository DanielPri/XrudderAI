from TileColor import TileColor


class Player:

    def __init__(self, board, name, color):
        self.board = board
        self.name = name
        self.color = color
        self.played_pieces = []
        self.max_tokens = 15
        self.max_moves = 30
        self.finished = False

    def play_turn(self, moves):
        played = False
        token_selected = False

        if len(self.played_pieces) == 0:
            choice = 1
        elif len(self.played_pieces) == self.max_tokens:
            print("You do not have any more tokens to place")
            choice = 2
        elif moves == self.max_moves:
            print("No more moves allowed")
            choice = 1
        else:
            print("Player", self.name, "Played Pieces", self.played_pieces)
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
            return 0
        elif choice is 2:
            print("Moves used: " + str(moves))
            if moves < self.max_moves:
                move_allowed = True
            else:
                if len(self.played_pieces) == self.max_tokens:
                    print(str(self.name) + " has no turns left!")
                    self.finished = True
                return 0
            while not token_selected:
                position = (input('Player ' + self.name + " select a token on the board: ")).upper().replace(" ", "")
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
                if self.compare_coordinates(position, new_position):
                    new_tile = self.select_tile(new_position)
                else:
                    continue

                if self.play_tile(new_tile):
                    tile.set_color(TileColor.BLANK)
                    self.played_pieces.remove(position)
                    self.played_pieces.append(new_position)
                    played = True
                    if move_allowed:
                        return 1


    @staticmethod
    def select_action():
        while 1 is 1:
            print("Choose an action")
            print("1. Place a token")
            print("2. Move a token")
            try:
                choice = int(input())
            except ValueError:
                print("Incorrect input. Please enter a number")
                continue
            if choice != 1 and choice != 2:
                print("Please enter a valid number")
                continue
            return choice

    def select_tile(self, position):
        if position and (position[0].isalpha() and position[1:].isdigit()):
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

    def compare_coordinates(self, position, new_position):
        letter_map = self.board.get_letter_map()
        if self.select_tile(new_position) is None:
            return False
        position_x = letter_map[position[0]]
        position_y = int(position[1])
        new_position_x = letter_map[new_position[0]]
        new_position_y = int(new_position[1])
        if position_x - 1 <= new_position_x <= position_x + 1:
            if position_y - 1 <= new_position_y <= position_y + 1:
                return True
            else:
                print("Cannot move more than one space in any direction")
                return False
        else:
            print("Cannot move more than one space in any direction")
            return False

