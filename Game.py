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
            except:
                print("Please Enter a valid number")
                continue

            if num_of_players <= 0 or num_of_players > 2:
                continue

            name = input("Please enter the name of player 1: ")
            self.player1 = Player(name, TileColor.WHITE)

            if num_of_players is 2:
                name = input("Please enter the name of player 2: ")
            else:
                name = "CPU"

            self.player2 = Player(name, TileColor.BLACK)

            break

    def play(self):
        self.board.draw()
        n = 1
        while n <= 30:
            print(self.player1.name, 'Turn', n)
            self.player1.play_turn(self.board)
            self.checkWinCondition()
            n += 1
            print(self.player2.name, 'Turn', n)
            self.player2.play_turn(self.board)
            self.checkWinCondition()
            n += 1
        print("GAME FINISHED")
        print("Game has reached the maximum number of turns!")

    def checkWinCondition(self):
        self.player1.playedPieces
        print("Player 1 Played Pieces", self.player1.playedPieces)
        self.player2.playedPieces
        print("Played 2 Played Pieces", self.player2.playedPieces)
        if len(self.player1.playedPieces) >= 5 or len(self.player2.playedPieces) >= 5:
            print("Checking for Win Condition")

# Testing if the board object works

# board.get_tile('E', 5).set_color(TileColor.BLACK)
# board.get_tile('I', 2).set_color(TileColor.WHITE)
# board.get_tile('A', 1).set_color(TileColor.WHITE)
# board.get_tile('C', 4).set_color(TileColor.WHITE)
# board.get_tile('A', 10).set_color(TileColor.WHITE)
# board.get_tile('M', 10).set_color(TileColor.WHITE)
# board.get_tile('M', 1).set_color(TileColor.WHITE)
# board.get_tile('A', 0)
# board.draw()
