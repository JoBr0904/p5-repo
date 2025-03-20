import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

screen_h = 800
screen_w = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Space Invaders. By josh')

#load imgs
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0, 0))

run = True

while run:
    clock.tick(fps)
    draw_bg()


    #event handers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
