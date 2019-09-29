from Tile import Tile


class Board:
    def __init__(self):
        rows, cols = (10, 13)
        self.tiles = [[Tile() for j in range(cols)] for i in range(rows)]
        self.letterMap = dict(A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11, M=12)

    def get_tile(self, row, col):
        row_value = self.letterMap[row]
        return self.tiles[col - 1][row_value]

    def draw(self):
        print()
        for i in range(len(self.tiles)):
            if i == 0:
                print(10 - i, end=' ')
            else:
                print(10 - i, end='  ')
            for j in range(len(self.tiles[0])):
                print(' ' + self.tiles[9 - i][j].get_color() + ' ', end='')
            print('\n   ------------------------------------------------------------------------------------------')
        print('     A      B      C      D      E      F      G      H      I      J      K      L      M')
