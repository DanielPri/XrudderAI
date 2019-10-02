from TileColor import TileColor


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def play_turn(self, board):
        tile = None
        while 1 is 1:
            try:
                print("Choose an action")
                print("1. Place a token")
                print("2. Move a token")
                choice = int(input())
            except:
                print("Please put the proper input")
                continue
            if choice != 1 and choice != 2:
                print("Please put the proper input")
                continue
            break

        while tile is None:
            if choice is 1:
                position = (input(self.name + " select a position to place your token: ")).upper().replace(" ", "")
                if position[0].isalpha() and position[1:].isdigit():
                    if board.is_valid_position(position[0], position[1:]):
                        tile = board.get_tile(position[0], position[1:])
                    else:
                        print("Please enter a valid tile")
                        continue

                if tile.get_color().value is not TileColor.BLANK.value:
                    print("That position is already occupied!")
                    tile = None
                else:
                    tile.set_color(self.color)
                    board.draw()
            elif choice is 2:
                position = (input(self.name + " select a token on the board: ")).upper().replace(" ", "")
                if position[0].isalpha() and position[1:].isdigit():
                    if board.is_valid_position(position[0], position[1:]):
                        tile = board.get_tile(position[0], position[1:])
                    else:
                        print("Please enter a valid tile")
                        continue

                if tile.get_color().value is self.color.value:
                    print("Choose a location to move token[", position, "]")
                    newPosition = (input()).upper().replace(" ", "")
                    if newPosition[0].isalpha() and newPosition[1:].isdigit():
                        if board.is_valid_position(newPosition[0], newPosition[1:]):
                            newTile = board.get_tile(newPosition[0], newPosition[1:])
                        else:
                            print("Please enter a valid tile")
                            tile = None
                            continue
                    if newTile.get_color().value is not TileColor.BLANK.value:
                        print("That position is already occupied!")
                        tile = None
                    else:
                        newTile.set_color(self.color)
                        tile.set_color(TileColor.BLANK)
                        board.draw()
                else:
                    print("wrong choice")
                    tile = None
                    continue
