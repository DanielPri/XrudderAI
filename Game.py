from Board import Board


board = Board()

board.draw()

board.get_tile('E', 5).set_black()
board.get_tile('I', 2).set_white()
board.draw()
