class Tile:
    def __init__(self):
        self.tileType = dict(color='____ ')

    def set_null(self):
        self.tileType['color'] = '____ '

    def set_white(self):
        self.tileType['color'] = 'white'

    def set_black(self):
        self.tileType['color'] = 'black'

    def get_color(self):
        return self.tileType['color']
