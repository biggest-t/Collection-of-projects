import pygame
import math
import sys
# import pain and suffering

# CONSTS
WINHEIGHT = 400
WINWIDTH = 800
OFFSET = 50

pygame_icon = pygame.image.load('D:\Programs\Renderer\death.jpg')
pygame.display.set_icon(pygame_icon)

SHAPE = [[0,0],[0,100], [100,100], [100, 0]]

for i in SHAPE:
    i[0] += 200
    i[1] += 200


def map_edge_to_vertex(SHAPE, EDGES, connect = True):
    length = len(SHAPE)
    for i in range(length):
        if i == length - 1 and connect == True:
            EDGES.append([SHAPE[i], SHAPE[0]])
        elif i != length -1:
            EDGES.append([SHAPE[i], SHAPE[i+1]])


pygame.init()

win = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

pygame.display.set_caption("2d wireframe renderer")

clock = pygame.time.Clock()
def draw_vertex(vertexList):
    for vert in vertexList:
        pygame.draw.circle(win, (0,0,0), (vert[0]  , vert[1]  ), 10)

def draw_lines(linesList):
    for line in linesList:
        pygame.draw.line(win, (174, 198, 247), (line[0][0] , line[0][1] ), (line[1][0] , line[1][1] ))




while True:
    # escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((100,100,100))
    EDGES = []

    map_edge_to_vertex(SHAPE, EDGES)
    # HOLYSHIT THE EDGES ARE REAL
    draw_lines(EDGES)
    draw_vertex(SHAPE)

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        btn=pygame.mouse

        move = True 
        for vert in range(len(SHAPE)):

          # for j in range(len(SHAPE)):
          #     if math.dist(SHAPE[vert], SHAPE[j]) < 10:
          #         move = False 

            distance = math.dist(pos, SHAPE[vert])
            if distance < 50 and move:
                SHAPE[vert] = pos
                break
            
    pygame.display.update()

    clock.tick(30)