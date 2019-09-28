class Board:
    def __init__(self):
        rows, cols = (10, 13)
        #Instead of initializing with zero, can initialize with Tile object which will be created in the future
        self.tiles = [[0]*cols]*rows
        self.letterMap = dict(A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11, M=12)

    def getTile(self, row, col):
        return self.tiles[self.letterMap[row]][col]

    def draw(self):
        print()
        for i in range(len(self.tiles)):
            if(i == 0):
                print(10 - i, end = ' ')
            else:
                print(10 - i, end='  ')
            for j in range(len(self.tiles[0])):
                print(' ' + str(self.tiles[i][j]) + ' ', end = '')
            print('\n   ---------------------------------------')
        print('   A  B  C  D  E  F  G  H  I  J  K  L  M')


board = Board()
print(board.getTile('J', 5))
board.draw()
