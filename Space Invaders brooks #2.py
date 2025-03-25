import pygame
from pygame.locals import *
# current time stamp 9:10 vidio 2
clock = pygame.time.Clock()
fps = 60

screen_h = 800
screen_w = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Space Invaders. By josh')

#cols
red = (255,0,0)
green = (0,255,0)


#load imgs
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0, 0))

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health

        
    def update(self):
        speed = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_w:
            self.rect.x += speed

        #draw health
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))


    

#sprite groups
spaceship_group = pygame.sprite.Group()


#player
spaceship = SpaceShip(int(screen_w / 2), screen_h - 100, 3)
spaceship_group.add(spaceship)





run = True

while run:
    clock.tick(fps)
    draw_bg()


    #event handers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    spaceship.update()

    spaceship_group.draw(screen)

    pygame.display.update()


pygame.quit()
