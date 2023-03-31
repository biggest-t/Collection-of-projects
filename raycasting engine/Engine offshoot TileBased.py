import pygame
import sys
import math

# CONSTS
SCREEN_HEIGHT =600
SCREEN_WIDTH = 600
MAP_SIZE = 8
TILE_SIZE = int(SCREEN_HEIGHT / MAP_SIZE)
    
# Globals
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2

player_ind = 0
player_row = 0
player_column = 0

# map
MAP = (
    '########'
    '# #    #'
    '# #  ###'
    '#      #'
    '# # C  #'
    '#   #  #'
    '#   #  #'
    '########'
)

# init pygame
pygame.init()

# create game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set window title
pygame.display.set_caption('offshoot')

# init timer
clock = pygame.time.Clock()

for row in range(8):
    for col in range(8):
        square = row * MAP_SIZE + col

        if MAP[square] == "C":
            player_ind = square
            player_row = row
            player_column = col



def draw_map():
    for row in range(8):
        for col in range(8):
            square = row * MAP_SIZE + col

            pygame.draw.rect(
                win,
                (200, 200, 200) if MAP[square] == '#' else (100, 100, 100),
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE -2 , TILE_SIZE -2 )
            )

    pygame.draw.rect(
            win,
            (0,255,0),
            (player_column * TILE_SIZE, player_row * TILE_SIZE, TILE_SIZE -2 , TILE_SIZE -2 )
        )



for i in range(8):
    for j in range(8):
        print(MAP[i * 8 + j], end = "")
    print()

# game loop
while True:
    # escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if MAP[player_ind - 1] != "#":
            player_ind -= 1
            player_column -= 1
    elif keys[pygame.K_RIGHT]:
        if MAP[player_ind + 1] != "#":
            player_ind += 1
            player_column += 1
    elif keys[pygame.K_UP]:
        if MAP[player_ind - 8] != "#":
            player_ind -= 8
            player_row -= 1
    elif keys[pygame.K_DOWN]:
        if MAP[player_ind + 8] != "#":
            player_ind += 8
            player_row += 1
    


    # draw 2D map
    draw_map()

    

    # update display
    pygame.display.flip()
    
    # set FPS
    clock.tick(30)
    