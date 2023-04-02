import render2d
import pygame
import sys
import numpy as np
from math import *


# so the idea i have is to do some trickery to make first rotate and project the points using maths and then use the 2d engine to draw the verticies

# hell i  got the idea,  use numpy to first rotate the matrices and then  convert the matrices to my shitty listed lists 

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

    box = render2d.render2d(projected_points, win)

    while True:
        win.fill((0))

        # escape condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()



        box.connect_with_wireframe()

        box.draw((255, 255,255))


        clock.tick(30)
        pygame.display.update()

if __name__ == "__main__":
    mainloop()

# good god gvim looks aweful yeah i'd rather use vs code than Gvim
