import pygame
import math
import sys

# import pain and suffering

"""
       legacy code :3

SHAPE = [[0,0,0],[0,100, 0], [100,100, 0], [100, 0, 0]]

Offset shape coords 
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

def draw_vertex(vertexList):
    for vert in vertexList:
        pygame.draw.circle(win, (0,0,0), (vert[0]  , vert[1]  ), 10)

def draw_lines(linesList):
    for line in linesList:
        pygame.draw.line(win, (174, 198, 247), (line[0][0] , line[0][1] ), (line[1][0] , line[1][1] ))

EDGES = []
map_edge_to_vertex(SHAPE, EDGES)
# HOLYSHIT THE EDGES ARE REAL
draw_lines(EDGES)
draw_vertex(SHAPE)
"""

# object oriented programming good

class render2d:
    def __init__(self, vertex: list, win):
        self.vertex = vertex 
        self.edges = [] 
        self.connect = True
        self.win = win
    
    def get_vertex(self):
        return self.vertex 

    def set_vertex(self, new_vertex: list):
        self.edges = new_vertex
    
    def get_edges(self):
        return self.edges
    
    def set_edges(self, new_edges: list):
        self.edges = new_edges

    def connect_with_wireframe(self):
        length = len(self.vertex)
        for i in range(length):
            if i == length - 1 and self.connect == True:
                self.edges.append([self.vertex[i], self.vertex[0]])
            elif i != length -1:
                self.edges.append([self.vertex[i], self.vertex[i+1]])
    
    def draw_vertex(self, color=(0)):
        for vert in self.vertex:
            pygame.draw.circle(self.win, color , (vert[0]  , vert[1]), 10)
    
    def draw_lines(self, color=(255, 255, 255)):
        for line in self.edges:
            pygame.draw.line(self.win, color , (line[0][0] , line[0][1] ), (line[1][0] , line[1][1] ))

    def draw(self, vert_color=(0), edges_color=(255, 255, 255)):
        self.draw_lines(edges_color)
        self.draw_vertex(vert_color)

        # reset edges so it doesn't keep appending and hogging memory
        self.set_edges([])
    
    def translate_x(self, amount: int):
        for i in self.vertex:
            i[0] += amount

    def translate_y(self, amount: int):
        for i in self.vertex:
            i[1] += amount

    def rotate(self, angle):
        pass

def mainloop():

    # CONSTS
    WINHEIGHT = 600
    WINWIDTH = 1000

    pygame_icon = pygame.image.load('D:\Programs\Renderer\death.jpg')
    pygame.display.set_icon(pygame_icon)

    pygame.init()

    win = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption("2d wireframe renderer")

    clock = pygame.time.Clock()

    # define all the shapes outside

    box = render2d([[0, 200], [200, 200], [200, 0], [0,0]], win)

    box.translate_x(100)

    box.translate_y(100)
    while True:
        # escape condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.fill((0))

        box.connect_with_wireframe()
        box.draw((255, 255, 255))


        box.rotate(math.pi / 2)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            move = True 


            vert_list = box.get_vertex()
            for vert in range(len(vert_list)):

                distance = math.dist(pos, [vert_list[vert][0], vert_list[vert][1]])
                if distance < 50 and move:
                    box.vertex[vert] = list(pos)
                    break
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]: box.translate_y(-10)
        if keys[pygame.K_DOWN]: box.translate_y(10)
        if keys[pygame.K_LEFT]: box.translate_x(-10)
        if keys[pygame.K_RIGHT]: box.translate_x(10)
                
        pygame.display.update()

        clock.tick(30)

if __name__ == "__main__":
    mainloop()