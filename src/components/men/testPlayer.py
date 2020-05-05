import pygame
from searchImage import search_image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # init
        self.image = pygame.image.load(search_image('images', 'p1_jump.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (800 / 2, 600 / 2)  # player position
        # default player speed value
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # default value for
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = +8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = +8

        self.rect.x += self.speedx
        self.rect.y += self.speedy
