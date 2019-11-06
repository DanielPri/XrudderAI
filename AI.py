from Board import Board

class AI:

    def __init__(self, color):
        self.color = color
        self.placed_tokens = []
        self.current_heuristic_value = None
        self.inverse_letter_map = None
        self.invert_letter_map()
    # ------------------------------------------------README--------------------------------------------------------
    # how this AI will work:
    # Decide next move creates a board with a token in A,1 tile
    # it runs heuristic_for_board on that board
    # it remembers the heuristic value for that move
    # it then makes a board with a token in A,2 and so on goes through the same steps until all tiles get a value
    # it then does that again by iterating through all its placed tokens (if there are any)
    #   and try all the possible moves for those tokens and see their heuristic values

    # Using the info from the current state of the board and whose turn it is, decide the next optimal move
    def decide_next_move(self, currentBoard, colorTurn):
        # based on whose turn it is, apply either a MIN or a MAX logic
        if colorTurn is self.color:
            # root is max
            print("in max root")
        else:
            # root is min
            print("in min root")

    def heuristic_for_board(self, boardScenario):
        # this function will evaluate the heuristic for a given game state
        print("evaluating Heuristic")
        self.board_loop(boardScenario, self.heuristic_for_tile)

    def heuristic_for_tile(self, tile, i, j):
        print("evaluating tile at" + self.inverse_letter_map[i] + j)
        # this function may need a isMax or isMin parameter as well
        # check how good this tile is
        #   how close is it to getting a legal X
        #   does it prevent enemy from winning
        # and compare it to currentHeuristicValue
        # if it's equal, check if it's nearer to the center
        # update currentHeuristicValue with the best heuristic value and at what location

    def board_loop(self, board, some_function):
        # loops through all board tiles, and performs a function at each one
        for i in range((len(self.inverse_letter_map))):
            for j in range(10):
                some_function(board.get_tile(self.inverse_letter_map[i], j+1), i, j+1)

    def invert_letter_map(self):
        board = Board()
        normal_letter_map = board.get_letter_map()
        self.inverse_letter_map = {v: k for k, v in normal_letter_map.items()}

