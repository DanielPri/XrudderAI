from Tile import Tile


class Board:
    def __init__(self):
        rows, cols = (10, 12)
        self.tiles = [[Tile() for _ in range(cols)] for _ in range(rows)]
        self.letterMap = dict(A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11)

    def get_letter_map(self):
        return self.letterMap

    def get_tile(self, row, col):
        return self.tiles[int(col) - 1][self.letterMap[row]]

    def draw(self):
        print()
        for i in range(len(self.tiles)):
            if i == 0:
                print(10 - i, end=' ')
            else:
                print(10 - i, end='  ')
            for j in range(len(self.tiles[0])):
                print(' ' + self.tiles[9 - i][j].get_color().value + ' ', end='')
            print('\n   -----------------------------------------------------------------------------------')
        print('     A      B      C      D      E      F      G      H      I      J      K      L')

    def is_valid_position(self, row, col):
        return row in self.letterMap and 0 < int(col) <= 10
