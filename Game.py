from Board import Board
from TileColor import TileColor
from Player import Player


class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.select_players()
        self.moves = 0
        self.play()

    def select_players(self):
        while 1 is 1:
            try:
                num_of_players = int(input("Please enter the number of human players (1 or 2): "))
            except ValueError:
                print("Please Enter a valid number")
                continue

            if num_of_players != 1 and num_of_players != 2:
                continue

            name = input("Please enter the name of player 1: ")
            self.player1 = Player(self.board, name, TileColor.WHITE)

            if num_of_players is 2:
                name = input("Please enter the name of player 2: ")
            else:
                name = "CPU"

            self.player2 = Player(self.board, name, TileColor.BLACK)

            break

    def play(self):
        self.board.draw()
        m = 1
        n = 1
        while True:
            if self.player1.finished and self.player2.finished:
                print("Game finished in a draw!")
                exit(0)
            print(self.player1.name, 'Turn', m)
            self.moves += self.player1.play_turn(self.moves)
            self.win_condition(self.player1)
            self.win_condition(self.player2)
            m += 1
            self.board.draw()
            print(self.player2.name, 'Turn', n)
            self.moves += self.player2.play_turn(self.moves)
            self.win_condition(self.player2)
            self.win_condition(self.player1)
            n += 1
            self.board.draw()

    def win_condition(self, player):

        letter_map = self.board.get_letter_map()
        letter_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

        if player == self.player1:

            for i in range(len(self.player1.played_pieces)):

                left_exists = False
                right_exists = False
                up_exists = False
                down_exists = False

                iterated_piece = str(self.player1.played_pieces[i])

                if iterated_piece[0] is not "A":
                    left_exists = True
                    west = letter_array[(letter_map[iterated_piece[0]] - 1)]
                    if iterated_piece[1] is not "10":
                        up_exists = True
                        north = int(iterated_piece[1]) + 1
                        top_left = self.board.get_tile(west, north)
                    if iterated_piece[1] is not "1":
                        down_exists = True
                        south = int(iterated_piece[1]) - 1
                        bottom_left = self.board.get_tile(west, south)
                    left = self.board.get_tile(west, int(iterated_piece[1]))
                if iterated_piece[0] is not "L":
                    right_exists = True
                    east = letter_array[(letter_map[iterated_piece[0]] + 1)]
                    if iterated_piece[1] is not "10":
                        up_exists = True
                        north = int(iterated_piece[1]) + 1
                        top_right = self.board.get_tile(east, north)
                    if iterated_piece[1] is not "1":
                        down_exists = True
                        south = int(iterated_piece[1]) - 1
                        bottom_right = self.board.get_tile(east, south)
                    right = self.board.get_tile(east, int(iterated_piece[1]))

                if left_exists and right_exists and up_exists and down_exists:
                    if top_left.get_color() == top_right.get_color() == bottom_left.get_color() == bottom_right.get_color() == TileColor.WHITE:
                        if left.get_color() == right.get_color() == TileColor.BLACK:
                            print("Strikethrough at white X centered at " + str(iterated_piece) + "!")
                        else:
                            print(str(self.player1.name) + " wins!")
                            exit(0)
                    elif top_left.get_color() == top_right.get_color() == bottom_left.get_color() == bottom_right.get_color() == TileColor.BLACK:
                        if left.get_color() == right.get_color() == TileColor.WHITE:
                            print("Strikethrough at white X centered at " + str(iterated_piece) + "!")
                        else:
                            print(str(self.player2.name) + " wins!")
                            exit(0)
        else:

            for i in range(len(self.player2.played_pieces)):

                left_exists = False
                right_exists = False
                up_exists = False
                down_exists = False

                iterated_piece = str(self.player2.played_pieces[i])

                if iterated_piece[0] is not "A":
                    left_exists = True
                    west = letter_array[(letter_map[iterated_piece[0]] - 1)]
                    if iterated_piece[1] is not "10":
                        up_exists = True
                        north = int(iterated_piece[1]) + 1
                        top_left = self.board.get_tile(west, north)
                    if iterated_piece[1] is not "1":
                        down_exists = True
                        south = int(iterated_piece[1]) - 1
                        bottom_left = self.board.get_tile(west, south)
                    left = self.board.get_tile(west, int(iterated_piece[1]))
                if iterated_piece[0] is not "L":
                    right_exists = True
                    east = letter_array[(letter_map[iterated_piece[0]] + 1)]
                    if iterated_piece[1] is not "10":
                        up_exists = True
                        north = int(iterated_piece[1]) + 1
                        top_right = self.board.get_tile(east, north)
                    if iterated_piece[1] is not "1":
                        down_exists = True
                        south = int(iterated_piece[1]) - 1
                        bottom_right = self.board.get_tile(east, south)
                    right = self.board.get_tile(east, int(iterated_piece[1]))

                if left_exists and right_exists and up_exists and down_exists:
                    if top_left.get_color() == top_right.get_color() == bottom_left.get_color() == bottom_right.get_color() == TileColor.WHITE:
                        if left.get_color() == right.get_color() == TileColor.BLACK:
                            print("Strikethrough at white X centered at " + str(iterated_piece) + "!")
                        else:
                            print(str(self.player1.name) + " wins!")
                            exit(0)
                    elif top_left.get_color() == top_right.get_color() == bottom_left.get_color() == bottom_right.get_color() == TileColor.BLACK:
                        if left.get_color() == right.get_color() == TileColor.WHITE:
                            print("Strikethrough at white X centered at " + str(iterated_piece) + "!")
                        else:
                            print(str(self.player2.name) + " wins!")
                            exit(0)
