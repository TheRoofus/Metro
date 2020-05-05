import pygame
import random
import os

# change your paths, when you refactor code!
game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, 'assets')
img_folder = os.path.join(assets_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png'))

# window size
WIDTH = 800
HEIGHT = 600
FPS = 30

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (51, 153, 255)
CORAL = (255, 127, 80)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # init
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # player position
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


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False
    # upload
    all_sprites.update()

    # Drawing
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
