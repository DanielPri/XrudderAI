from Board import Board
from Player import Player
from TileColor import TileColor
import copy
import random


class AI(Player):

    def __init__(self, board, name, color, opponent_color):
        super().__init__(board, name, color)
        self.opponent_color = opponent_color
        self.max_depth = 3
        self.best_moves = []
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

    def play_turn(self, moves, coin_toss):
        played = False

        if len(self.played_pieces) != 0:
            print("Player", self.name, "Played Pieces", self.played_pieces)
        self.best_moves = []  # reset the best moves
        imaginary_board = copy.deepcopy(self.board)
        if coin_toss == 2:  # AI goes second
            self.alpha_beta(imaginary_board, 1, -500000000000000000, 500000000000000000, False)
        else:  # AI goes first
            self.alpha_beta(imaginary_board, 1, -500000000000000000, 500000000000000000, True)
        print("Best moves for AI: " + str(self.best_moves))
        while not played:
            if not self.best_moves:
                print("No best moves available, skipping turn...")
                # played = True
                return 0
            else:
                position = random.choice(self.best_moves)
            if len(position) >= 5 and len(self.played_pieces) != 0:
                print("Moves used: " + str(moves))
                if len(position) == 5:
                    old_position = position[:2]
                    new_position = position[-2:]
                if len(position) == 6:
                    if position[2] == " ":
                        old_position = position[:2]
                        new_position = position[-3:]
                    if position[3] == " ":
                        old_position = position[:3]
                        new_position = position[-2:]
                if len(position) == 7:
                    old_position = position[:3]
                    new_position = position[-3:]
                if moves < self.max_moves:
                    move_allowed = True
                else:
                    if len(self.played_pieces) == self.max_tokens:
                        print(str(self.name) + " has no turns left!")
                        self.finished = True
                    return 0
                tile = self.select_tile(old_position)
                new_tile = self.select_tile(new_position)
                if self.play_tile(new_tile):
                    print("Proceeding to move a tile from " + str(old_position) + " to " + str(new_position))
                    tile.set_color(TileColor.BLANK)
                    self.played_pieces.remove(old_position)
                    self.played_pieces.append(new_position)
                    if move_allowed:
                        # played = True
                        return 1
            elif len(self.played_pieces) == self.max_tokens:
                print("AI does not have any more tokens to place")
                self.best_moves.remove(position)
            else:
                print("Proceeding to place a tile at " + str(position))
                self.play_tile(self.select_tile(position))
                self.played_pieces.append(position)
                # played = True
                return 0

    def alpha_beta(self, board, depth, alpha, beta, is_maximizing_player):
        # print('~~~~~~~~~~~~~~~~ imaginary board ~~~~~~~~~~~~~~~~ ')
        # board.draw()
        if depth is self.max_depth:
            return self.get_board_heuristic(board)

        if is_maximizing_player:
            best_value = alpha
            for number in range(1, len(self.board.tiles) + 1):
                for letter in self.board.letterMap:
                    if self.select_tile_on_imaginary_board(letter + str(number), board).get_color() != TileColor.BLANK \
                            and self.select_tile_on_imaginary_board(letter + str(number), board).get_color() == self.opponent_color:
                        # check the possible position to move the tile_token
                        self.check_max_moving_heuristic(letter, number, board, depth, alpha, best_value)
                    elif self.select_tile_on_imaginary_board(letter + str(number), board).get_color() == TileColor.BLANK \
                            and len(self.played_pieces) != self.max_tokens:  # place tokens only if it didn't play all tokens
                        new_board = self.play_imaginary_turn_placing(board, letter, number, self.opponent_color)
                        current_value = self.alpha_beta(new_board, depth + 1, alpha, beta, False)
                        if current_value > best_value:
                            # print("place " + letter + str(number))
                            # print("Current value: " + str(current_value))
                            best_value = current_value
                            self.best_moves.clear()
                            self.best_moves.append(letter + str(number))
                        elif current_value == best_value:
                            self.best_moves.append(letter + str(number))
                    else:
                        continue
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break
            return best_value
        else:
            best_value = beta
            for number in range(1, len(self.board.tiles) + 1):
                for letter in self.board.letterMap:
                    if self.select_tile_on_imaginary_board(letter + str(number), board).get_color() != TileColor.BLANK \
                            and self.select_tile_on_imaginary_board(letter + str(number), board).get_color() == self.color:
                        # check the possible position to move the tile_token
                        self.check_min_moving_heuristic(letter, number, board, depth, beta, best_value)
                    elif self.select_tile_on_imaginary_board(letter + str(number), board).get_color() == TileColor.BLANK \
                            and len(self.played_pieces) != self.max_tokens:  # place tokens only if it didn't play all tokens
                        new_board = self.play_imaginary_turn_placing(board, letter, number, self.color)
                        current_value = self.alpha_beta(new_board, depth + 1, alpha, beta, True)
                        if current_value < best_value:
                            # print("place " + letter + str(number))
                            # print("Current value: " + str(current_value))
                            best_value = current_value
                            self.best_moves.clear()
                            self.best_moves.append(letter + str(number))
                        elif current_value == best_value:
                            self.best_moves.append(letter + str(number))
                    else:
                        continue
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break
            return best_value

    def check_max_moving_heuristic(self, letter, number, board, depth, alpha, best_value):
        original_tile = letter + str(number)
        if original_tile in self.played_pieces:  # only consider moving if tile is in played pieces
            # top_left
            if board.is_valid_position((chr(ord(letter) - 1)), number + 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number + 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
            # left
            if board.is_valid_position((chr(ord(letter) - 1)), number):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number))
            # bottom_left
            if board.is_valid_position((chr(ord(letter) - 1)), number - 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number - 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number - 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number - 1))
            # bottom
            if board.is_valid_position(letter, number - 1):
                if self.select_tile_on_imaginary_board(letter + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, letter, number - 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + letter + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + letter + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + letter + str(number - 1))
            # bottom_right
            if board.is_valid_position((chr(ord(letter) + 1)), number - 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number - 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
            # right
            if board.is_valid_position((chr(ord(letter) + 1)), number):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number))
            # top right
            if board.is_valid_position((chr(ord(letter) + 1)), number + 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number + 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
            # top
            if board.is_valid_position(letter, number + 1):
                if self.select_tile_on_imaginary_board(letter + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, letter, number + 1, self.opponent_color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, alpha, best_value, False)
                    if current_value > best_value:
                        #print("move " + original_tile + " " + letter + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + letter + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + letter + str(number + 1))
        return best_value and self.best_moves

    def check_min_moving_heuristic(self, letter, number, board, depth, beta, best_value):
        original_tile = letter + str(number)
        if original_tile in self.played_pieces:  # only consider moving if tile is in played pieces
            # top_left
            if board.is_valid_position((chr(ord(letter) - 1)), number + 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number + 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number + 1))
            # left
            if board.is_valid_position((chr(ord(letter) - 1)), number):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number))
            # bottom_left
            if board.is_valid_position((chr(ord(letter) - 1)), number - 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) - 1) + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) - 1), number - 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) - 1) + str(number - 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) - 1) + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " +chr(ord(letter) - 1) + str(number - 1))
            # bottom
            if board.is_valid_position(letter, number - 1):
                if self.select_tile_on_imaginary_board(letter + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, letter, number - 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + letter + str(number - 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + letter + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + letter + str(number - 1))
            # bottom_right
            if board.is_valid_position((chr(ord(letter) + 1)), number - 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number - 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number - 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number - 1))
            # right
            if board.is_valid_position((chr(ord(letter) + 1)), number):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number))
            # top right
            if board.is_valid_position((chr(ord(letter) + 1)), number + 1):
                if self.select_tile_on_imaginary_board(chr(ord(letter) + 1) + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, chr(ord(letter) + 1), number + 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + chr(ord(letter) + 1) + str(number + 1))
            # top
            if board.is_valid_position(letter, number + 1):
                if self.select_tile_on_imaginary_board(letter + str(number + 1), board).get_color() == TileColor.BLANK:
                    new_board = self.play_imaginary_turn_moving(board, letter, number + 1, self.color, original_tile)
                    current_value = self.alpha_beta(new_board, depth + 1, beta, best_value, True)
                    if current_value < best_value:
                        #print("move " + original_tile + " " + letter + str(number + 1))
                        #print("Current value: " + str(current_value))
                        best_value = current_value
                        self.best_moves.clear()
                        self.best_moves.append(original_tile + " " + letter + str(number + 1))
                    elif current_value == best_value:
                        self.best_moves.append(original_tile + " " + letter + str(number + 1))
        return best_value and self.best_moves

    def play_imaginary_turn_placing(self, board, letter, number, color):
        board_copy = copy.deepcopy(board)
        self.place_tile_on_imaginary_board(self.select_tile_on_imaginary_board(letter + str(number), board_copy), color)
        return board_copy

    def play_imaginary_turn_moving(self, board, letter, number, color, original_tile):
        board_copy = copy.deepcopy(board)
        self.move_tile_on_imaginary_board(self.select_tile_on_imaginary_board(letter + str(number), board_copy), color, self.select_tile_on_imaginary_board(original_tile, board_copy))
        return board_copy

    @staticmethod
    def select_tile_on_imaginary_board(position, board):
        return board.get_tile(position[0], position[1:])

    @staticmethod
    def move_tile_on_imaginary_board(tile, color, original_tile):
        tile.set_color(color)
        original_tile.set_color(TileColor.BLANK)

    @staticmethod
    def place_tile_on_imaginary_board(tile, color):
        tile.set_color(color)

    @staticmethod
    def get_bottom_left_heuristic(board, letter, number, opponent_color):
        heuristic_value = 0
        if board.is_valid_position((chr(ord(letter) - 1)), number - 1):  # try the bottom left
            if board.get_tile((chr(ord(letter) - 1)), number - 1).get_color() == opponent_color:
                heuristic_value += 1
                if board.is_valid_position((chr(ord(letter) - 2)), number - 2):  # try bottom left of bottom left
                    if board.get_tile((chr(ord(letter) - 2)), number - 2).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) - 2)), number):  # try top left of the bottom left
                    if board.get_tile((chr(ord(letter) - 2)), number).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position(letter, number - 2):  # try bottom right of the bottom left
                    if board.get_tile(letter, number - 2).get_color() == opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    @staticmethod
    def get_top_left_heuristic(board, letter, number, opponent_color):
        heuristic_value = 0
        if board.is_valid_position((chr(ord(letter) - 1)), number + 1):  # try the top left
            if board.get_tile((chr(ord(letter) - 1)), number + 1).get_color() == opponent_color:
                heuristic_value += 1
                if board.is_valid_position((chr(ord(letter) - 2)), number):  # try bottom left of the top left
                    if board.get_tile((chr(ord(letter) - 2)), number).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) - 2)), number + 2):  # try top left of the top left
                    if board.get_tile((chr(ord(letter) - 2)), number + 2).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position(letter, number + 2): # try top right of the bottom left
                    if board.get_tile(letter, number + 2).get_color() == opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    @staticmethod
    def get_bottom_right_heuristic(board, letter, number, opponent_color):
        heuristic_value = 0
        if board.is_valid_position((chr(ord(letter) + 1)), number - 1):  # try the bottom right
            if board.get_tile((chr(ord(letter) + 1)), number - 1).get_color() == opponent_color:
                heuristic_value += 1
                if board.is_valid_position(letter, number - 2):  # try bottom left of the bottom right
                    if board.get_tile(letter, number - 2).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) + 2)), number):  # try top right of the bottom right
                    if board.get_tile((chr(ord(letter) + 2)), number).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) + 2)), number - 2):  # try bottom right of bottom right
                    if board.get_tile((chr(ord(letter) + 2)), number - 2).get_color() == opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    @staticmethod
    def get_top_right_heuristic(board, letter, number, opponent_color):
        heuristic_value = 0
        if board.is_valid_position((chr(ord(letter) + 1)), number + 1):  # try the top right
            if board.get_tile((chr(ord(letter) + 1)), number + 1).get_color() == opponent_color:
                heuristic_value += 1
                if board.is_valid_position(letter, number + 2):  # try top left of the top right
                    if board.get_tile(letter, number + 2).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) + 2)), number + 2):  # try top right of the top right
                    if board.get_tile((chr(ord(letter) + 2)), number + 2).get_color() == opponent_color:
                        heuristic_value += 1

                if board.is_valid_position((chr(ord(letter) + 2)), number):  # try bottom right of the top right
                    if board.get_tile((chr(ord(letter) + 2)), number).get_color() == opponent_color:
                        heuristic_value += 1
            return heuristic_value
        else:
            return -1

    def get_board_heuristic(self, board):
        total_heuristic = 0
        for number in range(1, len(board.tiles)+1):
            for letter in board.letterMap:
                if board.get_tile(letter, number).get_color() is not TileColor.BLANK:
                    current_color = board.get_tile(letter, number).get_color()
                    current_heuristic = 0
                    blocked = False

                    if board.is_valid_position((chr(ord(letter) - 1)), number - 1):  # try the bottom left
                        if board.get_tile((chr(ord(letter) - 1)), number - 1).get_color() == current_color:
                            current_heuristic += 1

                    if board.is_valid_position((chr(ord(letter) - 1)), number + 1):  # try top left
                        if board.get_tile((chr(ord(letter) - 1)), number + 1).get_color() == current_color:
                            current_heuristic += 1

                    if board.is_valid_position((chr(ord(letter) + 1)), number - 1):  # try bottom right
                        if board.get_tile((chr(ord(letter) + 1)), number - 1).get_color() == current_color:
                            current_heuristic += 1

                    if board.is_valid_position((chr(ord(letter) + 1)), number + 1):  # try top right
                        if board.get_tile((chr(ord(letter) + 1)), number + 1).get_color() == current_color:
                            current_heuristic += 1

                    # check block condition
                    if board.is_valid_position((chr(ord(letter) + 1)), number):  # try right
                        if board.get_tile((chr(ord(letter) + 1)), number).get_color() != current_color:
                            if board.is_valid_position((chr(ord(letter) - 1)), number):  # try left
                                if board.get_tile((chr(ord(letter) - 1)), number).get_color() != current_color:
                                    blocked = True

                    if current_heuristic == 4 and not blocked:
                        current_heuristic += 1000

                    if current_color is self.opponent_color:
                        total_heuristic += current_heuristic
                    else:
                        total_heuristic -= current_heuristic
        # print('heuristic value = ' + str(total_heuristic))
        return total_heuristic
