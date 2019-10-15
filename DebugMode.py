from TileColor import TileColor

def setBoard(board, p1, p2):
    board.get_tile("A", 1).set_color(TileColor.WHITE)
    board.get_tile("A", 3).set_color(TileColor.WHITE)
    board.get_tile("B", 2).set_color(TileColor.WHITE)
    board.get_tile("C", 1).set_color(TileColor.WHITE)
    board.get_tile("C", 3).set_color(TileColor.WHITE)
    board.get_tile("D", 5).set_color(TileColor.WHITE)
    board.get_tile("F", 5).set_color(TileColor.WHITE)
    board.get_tile("G", 5).set_color(TileColor.WHITE)
    board.get_tile("J", 1).set_color(TileColor.WHITE)
    board.get_tile("J", 3).set_color(TileColor.WHITE)
    board.get_tile("K", 2).set_color(TileColor.WHITE)
    board.get_tile("L", 1).set_color(TileColor.WHITE)

    p1.played_pieces = ["A1", "A3", "B2", "C1", "C3", "D5", "F5", "G5", "J1", "J3", "K2", "L1"]

    board.get_tile("A", 2).set_color(TileColor.BLACK)
    board.get_tile("C", 2).set_color(TileColor.BLACK)
    board.get_tile("D", 4).set_color(TileColor.BLACK)
    board.get_tile("D", 6).set_color(TileColor.BLACK)
    board.get_tile("E", 5).set_color(TileColor.BLACK)
    board.get_tile("F", 4).set_color(TileColor.BLACK)
    board.get_tile("F", 6).set_color(TileColor.BLACK)
    board.get_tile("G", 4).set_color(TileColor.BLACK)
    board.get_tile("G", 6).set_color(TileColor.BLACK)
    board.get_tile("H", 5).set_color(TileColor.BLACK)
    board.get_tile("J", 2).set_color(TileColor.BLACK)
    board.get_tile("I", 4).set_color(TileColor.BLACK)

    p2.played_pieces = ["A2", "C2", "D4", "D6", "E5", "F4", "F6", "G4", "G6", "H5", "J2", "I4"]


