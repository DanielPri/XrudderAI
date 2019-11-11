from Board import Board
from Player import Player
from TileColor import TileColor


class AI(Player):

    def __init__(self, board, name, color, opponent_color):
        super().__init__(board, name, color)
        self.opponent_color = opponent_color
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

    def play_turn(self, moves):
        heuristic_value = 0
        position_to_play = None
        for number in range(1, len(self.board.tiles)+1):
            for letter in self.board.letterMap:
                if self.board.get_tile(letter, number).get_color() == TileColor.BLANK:
                    bottom_left_heuristic = self.get_bottom_left_heuristic(letter, number)
                    top_left_heuristic = self.get_top_left_heuristic(letter, number)
                    bottom_right_heuristic = self.get_bottom_right_heuristic(letter, number)
                    top_right_heuristic = self.get_top_right_heuristic(letter, number)

                    current_heuristic = 0
                    if bottom_left_heuristic > 0:
                        current_heuristic += bottom_left_heuristic
                    if top_left_heuristic > 0:
                        current_heuristic += top_left_heuristic
                    if bottom_right_heuristic > 0:
                        current_heuristic += bottom_right_heuristic
                    if top_right_heuristic > 0:
                        current_heuristic += top_right_heuristic

                    if current_heuristic > heuristic_value:
                        position_to_play = letter + str(number)

        if position_to_play is not None:
            self.play_tile(self.select_tile(position_to_play))
        return 0

    def get_bottom_left_heuristic(self, letter, number):
        heuristic_value = 0
        if self.board.is_valid_position((chr(ord(letter) - 1)), number - 1):  # try the bottom left
            if self.board.get_tile((chr(ord(letter) - 1)),
                                   number - 1).get_color() == self.opponent_color:
                heuristic_value += 1
                if self.board.is_valid_position((chr(ord(letter) - 2)), number - 2):  # try bottom left of bottom left
                    if self.board.get_tile((chr(ord(letter) - 2)),
                                           number - 2).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) - 2)), number):  # try top left of the bottom left
                    if self.board.get_tile((chr(ord(letter) - 2)),
                                           number).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position(letter, number - 2):  # try bottom right of the bottom left
                    if self.board.get_tile(letter,
                                           number - 2).get_color() == self.opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    def get_top_left_heuristic(self, letter, number):
        heuristic_value = 0
        if self.board.is_valid_position((chr(ord(letter) - 1)), number + 1):  # try the top left
            if self.board.get_tile((chr(ord(letter) - 1)),
                                   number + 1).get_color() == self.opponent_color:
                heuristic_value += 1
                if self.board.is_valid_position((chr(ord(letter) - 2)), number):  # try bottom left of the top left
                    if self.board.get_tile((chr(ord(letter) - 2)),
                                           number).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) - 2)), number + 2):  # try top left of the top left
                    if self.board.get_tile((chr(ord(letter) - 2)),
                                           number + 2).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position(letter, number + 2): # try top right of the bottom left
                    if self.board.get_tile(letter,
                                           number + 2).get_color() == self.opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    def get_bottom_right_heuristic(self, letter, number):
        heuristic_value = 0
        if self.board.is_valid_position((chr(ord(letter) + 1)), number - 1):  # try the bottom right
            if self.board.get_tile((chr(ord(letter) + 1)),
                                   number - 1).get_color() == self.opponent_color:
                heuristic_value += 1
                if self.board.is_valid_position(letter, number - 2):  # try bottom left of the bottom right
                    if self.board.get_tile(letter,
                                           number - 2).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) + 2)), number):  # try top right of the bottom right
                    if self.board.get_tile((chr(ord(letter) + 2)),
                                           number).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) + 2)), number - 2):  # try bottom right of bottom right
                    if self.board.get_tile((chr(ord(letter) + 2)),
                                           number - 2).get_color() == self.opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    def get_top_right_heuristic(self, letter, number):
        heuristic_value = 0
        if self.board.is_valid_position((chr(ord(letter) + 1)), number + 1):  # try the top right
            if self.board.get_tile((chr(ord(letter) + 1)),
                                   number + 1).get_color() == self.opponent_color:
                heuristic_value += 1
                if self.board.is_valid_position(letter, number + 2):  # try top left of the top right
                    if self.board.get_tile(letter,
                                           number + 2).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) + 2)), number + 2):  # try top right of the top right
                    if self.board.get_tile((chr(ord(letter) + 2)),
                                           number + 2).get_color() == self.opponent_color:
                        heuristic_value += 1

                if self.board.is_valid_position((chr(ord(letter) + 2)), number):  # try bottom right of the top right
                    if self.board.get_tile((chr(ord(letter) + 2)),
                                           number).get_color() == self.opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1