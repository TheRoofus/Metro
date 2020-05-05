import pygame
from searchImage import search_image


class FirstTrain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # init
        self.image = pygame.image.load(search_image('trains', 'sprite_traincars0.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)  # player position
        # default player speed value
        self.speedx = 0

    def update(self):
        # default value for
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = +8

        self.rect.x += self.speedx
