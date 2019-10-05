from Board import Board
from TileColor import TileColor
from Player import Player


class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.select_players()
        self.play()
        self.turns = 0

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
        n = 1
        while n <= 30:
            print(self.player1.name, 'Turn', n)
            self.player1.play_turn()
            self.win_condition()
            n += 1
            print(self.player2.name, 'Turn', n)
            self.player2.play_turn()
            self.win_condition()
            n += 1
        print("GAME FINISHED")
        print("Game has reached the maximum number of turns!")

    def win_condition(self):
        self.player1.played_pieces
        print("Player", self.player1.name, "Played Pieces", self.player1.played_pieces)
        self.player2.played_pieces
        print("Played", self.player2.name, "Played Pieces", self.player2.played_pieces)
        if len(self.player1.played_pieces) >= 5 or len(self.player2.played_pieces) >= 5:
            print("Checking for Win Condition")
