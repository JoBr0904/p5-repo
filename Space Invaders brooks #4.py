import pygame
from pygame.locals import *
import random
clock = pygame.time.Clock()
fps = 60

screen_h = 800
screen_w = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Space Invaders. By josh')

#game variables
rows = 5
cols = 5

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
        self.last_shot = pygame.time.get_ticks()

        
    def update(self):
        speed = 8
        #cooldown
        cooldown = 500 #milliseconds
        #key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_w:
            self.rect.x += speed

        time_now = pygame.time.get_ticks()
        #shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now


        #draw health
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -=5
        if self.rect.bottom < 0:
            self.kill()







class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/alien" + str(random.randint(1,5)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
             self.move_direction *= -1
             self.move_counter *= self.move_direction


    

#sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()



def create_aliens():
    #generate aliens
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)

create_aliens()

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

    # update the groups
    bullet_group.update()
    alien_group.update()
    
    # draw the groups
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)

    pygame.display.update()


pygame.quit()
