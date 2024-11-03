import pygame
import util
colors = {"white": (255, 255, 255),
        "black": (0, 0, 0)
}

def get_upper_left(tiles_dict, pos):
    """ return the tiles at the upper lef or none """
    x, y = pos[0] - 1, pos[1] - 1
    return tiles_dict.get((x, y), None)

def get_upper_right(tiles_dict, pos):
    x, y = pos[0] - 1, pos[1] + 1
    return tiles_dict.get((x, y), None)

def get_lower_left(tiles_dict, pos):
    x, y = pos[0] + 1, pos[1] - 1
    return tiles_dict.get((x, y), None)

def get_lower_right(tiles_dict, pos):
    x, y = pos[0] + 1, pos[1] + 1
    return tiles_dict.get((x, y), None)


class Tile(pygame.Rect):
    """ create a new tile as rectangle """
    def __init__(self, x, y, pos, width=80, height=80,):
        """initialize a new rectangle """
        super().__init__(x, y, width, height)
        self.has_piece = False
        self.pos = pos
        self._color = None
        self.piece = None
        self.upper_left = None
        self.upper_right = None
        self.lower_left = None
        self.lower_right = None
        self.prev = None
        self.next = None


        self.color = None
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if (self.pos[0] + self.pos[1]) % 2 == 0:
            self._color = "white"
        else:
            self._color = "black"

    def can_be_taken(self, tile, des):
        """ return true if piece can be taken in a given direction """
        directions = ["upper_left", "upper_right", "lower_left", "lower_right"]
        for d in directions:
            if getattr(self, d) is not None:
                dis = tile.pos[0] + self.pos[0]
                print(tile.pos, tile.has_piece)
                #print(getattr(self, d).has_piece == False and dis % 2 == 1)
                return getattr(self, d).has_piece == False and dis % 2 == 1
            return False


class Piece:
    """ This class describes a piece """
    def __init__(self, color, filename):
        """ initialize a new piece """
        self.image = pygame.image.load(filename)
        self.color = color
        self.owner = f"{color}_player"
        self.is_king = False
        self.is_taken = False
        self.size = 70

        self.image = pygame.transform.scale(self.image, (self.size, self.size))


class Board:
    def __init__(self, screen, board, board_size, tile_size=80):
        self.screen = screen
        self.board = board
        self.board_size = board_size
        self.tile_size = tile_size
        self.num_moves = 0
        self.moves = []

        self.tiles, self.tile_dict = self.draw()

    def draw(self):
        tiles = []
        tiles_dict = {}
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                x = (1.5 * self.tile_size) + j * self.tile_size
                y = self.tile_size + i * self.tile_size

                rect = Tile(x, y, (i, j),
                    self.tile_size, self.tile_size,
                    )
                tiles_dict[(i, j)] = rect
                pygame.draw.rect(self.screen, colors[rect.color], rect)
                row.append(rect)
                if self.board[i][j]:
                    if self.board[i][j] == "W":
                        piece = Piece("white", "white_prev_ui.png")
                    else:
                        piece = Piece("black", "blackf_prev_ui.png")
                    piece_x = rect.x + (rect.width - piece.size) // 2
                    piece_y = rect.y + (rect.height - piece.size) // 2
                    rect.piece = piece
                    rect.has_piece = True
                    self.screen.blit(piece.image, (piece_x, piece_y))

            tiles.append(row)
        for key, value in tiles_dict.items():
            value.upper_left = get_upper_left(tiles_dict, value.pos)
            value.upper_right = get_upper_right(tiles_dict, value.pos)
            value.lower_left = get_lower_left(tiles_dict, value.pos)
            value.lower_right = get_lower_right(tiles_dict, value.pos)


        return tiles, tiles_dict

    def get_player(self):
        if self.num_moves % 2 == 0:
            return "white"
        return "black"
