import pygame
import util
from tile import Tile, Piece, Board

# initialize variables
black = (0, 0, 0)
white = (255, 255, 255)
board_size = 8
tile_size = 80

board = util.init_board(board_size)

colors = [white, black]
num_colors = len(colors)

screen_size = screen_width, screen_height = 800, 700

board_width, board_height = 500, 500

pygame.init()

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)

largefont = pygame.font.Font("OpenSans-Regular.ttf", 60)
screen = pygame.display.set_mode(screen_size)

tiles_clicked = []
pos_clicked = []
tiles_to_image = {}
running = True

moves = []
game_board = Board(screen, board, board_size, tile_size)
tiles = game_board.tiles
points = []

def get_directions(tile):
    """ get directions that cam be move to """
    neighbours = [tile.upper_left, tile.upper_right, tile.lower_left, tile.lower_right]
    sides = ["upper_left", "upper_right", "lower_left", "lower_right"]
    directions = []
    for neighbour in neighbours:
        if neighbour:
            if neighbour.has_piece and neighbour.piece.color != game_board.get_player() and neighbour != tiles_clicked[0]:
                #print(game_board.get_player())
                for side in sides:
                    if (getattr(tile, side) == neighbour 
                            and neighbour.can_be_taken(tiles_clicked[0], side)
                            and getattr(neighbour, side) not in points):
                        print(tiles_clicked[0].has_piece)
                        tile.next = neighbour
                        neighbour.prev = tile
                        neighbour.next = getattr(neighbour, side)
                        print(f"tile {tile.pos} appends {neighbour.next.pos} through {neighbour.pos} at {side}")
                        #setattr(neighbour, side, getattr(neighbour
                        directions.append(neighbour.next)
            if not neighbour.has_piece and tile.has_piece:
                if (tile.piece.color == "white" and tile.pos[0] > neighbour.pos[0]) or (tile.piece.color == "black" and tile.pos[0] < neighbour.pos[0]) or tile.piece.is_king:
                    print(f"tile {tile.pos} appends {neighbour.pos}")
                    tile.next = neighbour
                    neighbour.prev = tile
                    directions.append(neighbour)
    return directions


def get_moves(tile):
    """ get possible moves """
    moves = {}
    routes = []
    frontier = []
    frontier.append(tile)
    while True:
        if len(frontier) < 1:
            break
        tile = frontier.pop()
        for direction in get_directions(tile):
            #direction.prev = tile
            #tile.next = direction
            frontier.append(direction)

            routes.append(direction)
    return routes


def get_pos_and_tiles(mouse):
    """Returns the position clicked and tile at the position"""

    for i in range(board_size):
            for j in range(board_size):
                if tiles[i][j].collidepoint(mouse):
                    return (i, j), tiles[i][j]

def handle_keydown(event):
    if event.button == 1:
        mouse = pygame.mouse.get_pos()

        pos, tile = get_pos_and_tiles(mouse)

        if len(tiles_clicked) == 0 and tile.has_piece and tile.color == "white":

            tiles_clicked.append(tile)
            pos_clicked.append(pos)
            game_board.moves = get_moves(tile)

        elif len(tiles_clicked) == 1 and tile.color == "white":
            if tile.has_piece:
                tiles_clicked.clear()
                pos_clicked.clear()

            tiles_clicked.append(tile)
            pos_clicked.append(pos)

        elif tile.color == "black":
            tiles_clicked.clear()
            pos_clicked.clear()
        if len(tiles_clicked) == 2:
            PLAYER = game_board.get_player()
            tile_1, tile_2 = tiles_clicked
            x_1, y_1 = pos_clicked[0]
            x_2, y_2 = pos_clicked[1]

            if tile_2 in game_board.moves:
                t = tile_2
                while t is not tile_1:
                    if t.has_piece:
                        t.has_piece = False
                        t.piece = None
                        x, y = t.pos
                        board[x][y] = util.EMPTY
                    t = t.prev


            #print("3: ", tiles_clicked)
                board[x_2][y_2] = board[x_1][y_1]
                board[x_1][y_1] = util.EMPTY
                tile_2.has_piece = tile_1.has_piece
                tile_2.piece = tile_1.piece
                tile_1.piece = None
                tile_1.has_piece = False

            tiles_clicked.clear()
            pos_clicked.clear()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_keydown(event)

    screen.fill(black)
    title = largefont.render("Checker", True, white)
    titleRect = title.get_rect()
    titleRect.center = ((screen_width / 2), 50)
    screen.blit(title, titleRect)

    # draw board
    
    tile_origin = (120, 80)
    board_rect = pygame.Rect(
        120, 80, 480, board_size * tile_size)
    game_board.draw()


    pygame.draw.rect(screen, white, board_rect, 5)

    
    pygame.display.flip()
