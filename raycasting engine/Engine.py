import pygame
import sys
import math

# CONSTS
SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 20
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)

MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)

FOV = math.pi / 3
HALF_FOV = FOV / 2

CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS

SCALE = SCREEN_HEIGHT / CASTED_RAYS
# Globals VARS
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi 

# map
MAP = (
    '####################'
    '#$$$$$$#    # ###  #'
    '#$$$$$$#    #      #'
    '#$$$$$$#    #      #'
    '#$$$$$$            #'
    '#$$$$$$      ##    #'
    '#######           ##'
    '#     #        #####'
    '#     #            #'
    '#     #      #######'
    '#     #            #'
    '#                  #'
    '#              #####'   
    '#  #        #      #'
    '#  #        #      #'
    '# #         #      #'
    '# #####     #      #'
    '#           #      #'
    '#           ##  #  #'
    '####################'
)

# init pygame
pygame.init()

# create game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set window title
pygame.display.set_caption('Raycasting')

# init timer
clock = pygame.time.Clock()

def draw_map():
    for row in range(MAP_SIZE):
        for col in range(MAP_SIZE):
            square = row * MAP_SIZE + col

            bl_color = (0)

            pygame.draw.rect(
                win,
                bl_color,
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE -2 , TILE_SIZE -2 )
            )
    
    pygame.draw.circle(win, (255, 0, 0), (int(player_x), int(player_y)), 16)


   ### draw dir

   #pygame.draw.line(win, (0,0,255), (player_x, player_y), (player_x - math.sin(player_angle) * TILE_SIZE , player_y + math.cos(player_angle) * TILE_SIZE), 3)
   #
   ### draw FOV

   #pygame.draw.line(win, (0, 220, 255), (player_x, player_y), (player_x - math.sin(player_angle - HALF_FOV) * TILE_SIZE , player_y + math.cos(player_angle - HALF_FOV) * TILE_SIZE), 3)
   #pygame.draw.line(win, (0, 220, 255), (player_x, player_y), (player_x - math.sin(player_angle + HALF_FOV) * TILE_SIZE , player_y + math.cos(player_angle + HALF_FOV) * TILE_SIZE), 3)


# money folder

def cast_rays():

    # left most angle
    start_angle = player_angle - HALF_FOV

    # loop over casted rays
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            
            target_x = int(player_x - math.sin(start_angle) * depth )
            target_y = int(player_y + math.cos(start_angle) * depth )

            # covert target X, Y coordinate to map col, row
            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)

            # calculate map square index
            square = row * MAP_SIZE + col

            if MAP[square] == '#':
                pygame.draw.rect(win, (255, 100, 100), (col * TILE_SIZE,
                                                    row * TILE_SIZE,
                                                    TILE_SIZE - 2,
                                                    TILE_SIZE - 2))

                pygame.draw.line(win, (0, 0, 255), (player_x, player_y), (target_x, target_y))

                # wall color

                color = int(255  / (1 + depth * depth * 0.0001))
                # calc wall height

                # fish eye fix
                depth *= math.cos(player_angle - start_angle)

                wall_height = 21000 / (depth + 0.0001)

                # potential freeze bug fix

                if wall_height > SCREEN_HEIGHT:
                    wall_height = SCREEN_HEIGHT

                # draw projection illusion big jaw yee ahhs (rect by rect)

                pygame.draw.rect(win, (color, color, color), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height /2, SCALE, wall_height))

                break
            

        start_angle += STEP_ANGLE

        
forward = True
# game loop
while True:
    # escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # goose mode
    col = int(player_x / TILE_SIZE)
    row = int(player_y / TILE_SIZE)

    # calculate player square index
    square = row * MAP_SIZE + col

    # colission
    if MAP[square] == '#':
        if forward:
            player_x -= -math.sin(player_angle) *3
            player_y -= math.cos(player_angle)*3
        else:
            player_x += -math.sin(player_angle) *3
            player_y += math.cos(player_angle)*3

 
    # update backg 

    pygame.draw.rect(win, (0), (0,0,SCREEN_HEIGHT, SCREEN_HEIGHT))

    # update 3d backg
    pygame.draw.rect(win, (100, 100, 100), (SCREEN_HEIGHT,SCREEN_HEIGHT/2, SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.draw.rect(win, (9,160, 255), (SCREEN_HEIGHT,-SCREEN_HEIGHT/2, SCREEN_HEIGHT, SCREEN_HEIGHT))

    # draw 2D map
    draw_map()

    # cast
    cast_rays()

    # control shit
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: player_angle -= 0.1
    if keys[pygame.K_RIGHT]: player_angle += 0.1
    if keys[pygame.K_UP]:
        forward = True
        player_x += -math.sin(player_angle) *3
        player_y += math.cos(player_angle)*3
    if keys[pygame.K_DOWN]:
        forward = False
        player_x -= -math.sin(player_angle)*3
        player_y -= math.cos(player_angle)*3

    clock.tick(30)



    # update display
    pygame.display.flip()
    