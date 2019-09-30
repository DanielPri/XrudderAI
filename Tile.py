from TileColor import TileColor


class Tile:
    def __init__(self):
        self.tileColor = TileColor.BLANK

    def set_color(self, tile_color):
        self.tileColor = tile_color

    def get_color(self):
        return self.tileColor
