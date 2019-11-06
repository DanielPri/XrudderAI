from Board import Board

class AI:

    def __init__(self, color):
        self.color = color
        self.placed_tokens = []
        # heuristic NODE with both a numerical value, and a decision type (move, place or none)
        self.current_heuristic_value = None
        self.inverse_letter_map = None
        self.invert_letter_map()
    # ------------------------------------------------README--------------------------------------------------------
    # how this AI will work:
    # Decide next move creates a board with a token in first unoccupied tile
    # it will do it for whoever's turn it is, and will do a MIN or MAX accordingly
    # it runs heuristic_for_board on that board
    # it remembers the heuristic value for that board in current_heuristic_value
    # it loops: makes a board with a token in the second unoccupied tile
    # goes through the same steps, replacing previous current_heuristic_value if better are found
    # it then does that again by iterating through all its placed tokens (if there are any)
    #   and try all the possible moves for those tokens and see their heuristic values
    #   (remember, moves are different from placing)
    # at the end, the current_heuristic_value with the best value will be the one used to create the move

    # Using the info from the current state of the board and whose turn it is, decide the next optimal move
    def decide_next_move(self, current_board, color_turn):
        # based on whose turn it is, apply either a MIN or a MAX logic
        if color_turn is self.color:
            # root is max
            print("in max root")
        else:
            # root is min
            print("in min root")
            # hardcoded to G6 for now
        return "G6"

    def heuristic_for_board(self, board_scenario):
        # this function will evaluate the heuristic for a given game state
        print("evaluating Heuristic")
        self.board_loop(board_scenario, self.heuristic_for_tile)

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

