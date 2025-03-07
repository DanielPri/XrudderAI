from Board import Board
from Player import Player
from AI import AI
from DebugMode import *


class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.moves = 0
        self.game_over = False
        self.AI = None
        self.select_players()

    def select_players(self):
        while 1 is 1:
            try:
                num_of_players = int(input("Please enter the number of human players (1 or 2): "))
            except ValueError:
                print("Please Enter a valid number")
                continue

            if num_of_players != 1 and num_of_players != 2 and num_of_players != 42:
                continue

            name = input("Please enter the name of player 1: ")
            self.player1 = Player(self.board, name, TileColor.WHITE)

            if num_of_players is 2:
                name = input("Please enter the name of player 2: ")
                self.player2 = Player(self.board, name, TileColor.BLACK)
                self.play()
            else:
                name = "CPU"
                self.AI = AI(self.board, name, TileColor.BLACK, TileColor.WHITE)
                self.play_with_ai()

            if num_of_players is 42:
                print("\n\n\n\n\n")
                print("-----------------------------WELCOME TO DEBUG MODE----------------------------------------")
                print("------------------------------------------------------------------------------------------")
                self.moves = 28
                set_board(self.board, self.player1, self.player2)
                self.play()

            break

    def play(self):
        player1_turn = 1
        player2_turn = 1
        while True:
            self.board.draw()
            if self.player1.finished and self.player2.finished:
                print("Game finished in a draw!")
                self.game_over = True
                break
            print("Player " + self.player1.name, 'Turn', player1_turn)
            current_moves = self.moves
            self.moves += self.player1.play_turn(self.moves)
            if len(self.player1.played_pieces) >= 5 or len(self.player2.played_pieces) >= 5:
                self.win_condition(self.player1.name, self.player1.played_pieces, self.player1.color, self.player2.color)
                if self.game_over:
                    break
                elif not current_moves == self.moves:
                    self.win_condition(self.player2.name, self.player2.played_pieces, self.player2.color, self.player1.color)
                    if self.game_over:
                        break
            player1_turn += 1

            self.board.draw()
            print("Player " + self.player2.name, 'Turn', player2_turn)
            current_moves = self.moves
            self.moves += self.player2.play_turn(self.moves)
            if len(self.player1.played_pieces) >= 5 or len(self.player2.played_pieces) >= 5:
                self.win_condition(self.player2.name, self.player2.played_pieces, self.player2.color, self.player1.color)
                if self.game_over:
                    break
                elif not current_moves == self.moves:
                    self.win_condition(self.player1.name, self.player1.played_pieces, self.player1.color, self.player2.color)
                    if self.game_over:
                        break
            player2_turn += 1

    def play_with_ai(self):
        player1_turn = 1
        ai_turn = 1
        while True:
            self.board.draw()
            if self.player1.finished and self.AI.finished:
                print("Game finished in a draw!")
                self.game_over = True
                break
            print("Player " + self.player1.name, 'Turn', player1_turn)
            current_moves = self.moves
            self.moves += self.player1.play_turn(self.moves)
            if len(self.player1.played_pieces) >= 5 or len(self.AI.played_pieces) >= 5:
                self.win_condition(self.player1.name, self.player1.played_pieces, self.player1.color, self.AI.color)
                if self.game_over:
                    break
                elif not current_moves == self.moves:
                    self.win_condition(self.AI.name, self.AI.played_pieces, self.AI.color, self.player1.color)
                    if self.game_over:
                        break
            player1_turn += 1

            self.board.draw()
            print("Player " + self.AI.name, 'Turn', ai_turn)
            current_moves = self.moves
            self.moves += self.AI.play_turn(self.moves)
            if len(self.player1.played_pieces) >= 5 or len(self.AI.played_pieces) >= 5:
                self.win_condition(self.AI.name, self.AI.played_pieces, self.AI.color, self.player1.color)
                if self.game_over:
                    break
                elif not current_moves == self.moves:
                    self.win_condition(self.player1.name, self.player1.played_pieces, self.player1.color, self.AI.color)
                    if self.game_over:
                        break
            ai_turn += 1

    def win_condition(self, name, played_pieces, player_color, opponent_color):
        letter_map = self.board.get_letter_map()
        letter_array = []

        for key in letter_map.keys():
            letter_array.append(key)

        for i in range(len(played_pieces)):
            # booleans track if current piece is on the edge of the board
            left_exists = False
            right_exists = False
            up_exists = False
            down_exists = False

            iterated_piece = str(played_pieces[i])

            # Checks edge cases
            if iterated_piece[0] is not "A":
                left_exists = True
                west = letter_array[(letter_map[iterated_piece[0]] - 1)]
                if int(iterated_piece[1:]) is not 10:
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
                if int(iterated_piece[1:]) is not 10:
                    up_exists = True
                    north = int(iterated_piece[1]) + 1
                    top_right = self.board.get_tile(east, north)
                if iterated_piece[1] is not "1":
                    down_exists = True
                    south = int(iterated_piece[1]) - 1
                    bottom_right = self.board.get_tile(east, south)
                right = self.board.get_tile(east, int(iterated_piece[1]))

            if left_exists and right_exists and up_exists and down_exists:
                if top_left.get_color() == top_right.get_color() == bottom_left.get_color() == bottom_right.get_color() == player_color:
                    if left.get_color() == right.get_color() == opponent_color:
                        print("Strikethrough at " + str(player_color)[10:15] + " X centered at " + str(iterated_piece) + "!")
                    else:
                        self.board.draw()
                        print("Player " + name + " wins!")
                        self.game_over = True
                        break
