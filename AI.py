from Board import Board

class AI:

    def __init__(self, color):
        self.color = color
        self.prediction_board = Board()
        self.placedTiles = []
        self.letter_map = self.prediction_board.get_letter_map()


    # Using the info from the current state of the board and whose turn it is, decide the next optimal move
    def decide_next_move(self, currentBoard, colorTurn):
        # based on whose turn it is, apply either a MIN or a MAX logic
        if colorTurn is self.color:
            # root is max
        else:
            # root is min

    def heuristic(self, boardScenario):
        # this function will evaluate the heuristic for a given game state