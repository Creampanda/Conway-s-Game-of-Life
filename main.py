import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 1500,1000
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
white = (255, 255, 255)

scaler = 10
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.rand2d_array()
# Grid.make_glider(4,4)

run = True

while run:
    clock.tick(fps)
    screen.fill(black)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color=black, on_color=white, surface=screen)
    pygame.display.update()