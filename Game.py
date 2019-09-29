from Board import Board


board = Board()

board.draw()

# Testing if the board object works

board.get_tile('E', 5).set_black()
board.get_tile('I', 2).set_white()
board.get_tile('A', 1).set_white()
board.get_tile('C', 4).set_white()
board.get_tile('A', 10).set_white()
board.get_tile('M', 10).set_white()
board.get_tile('M', 1).set_white()
board.draw()
