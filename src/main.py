import pygame

from Media.colors import colors
from Logic.trains.firstTrain import FirstTrain
from Logic.men.testPlayer import Player
from lib.variables import WIDTH, HEIGHT, FPS
from searchImage import search_image

import os

"""
Создание основных окон и запуск модулей для последующего 
выполнения в приложении.
"""

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(FirstTrain())
all_sprites.add(Player())

background = pygame.image.load(search_image('space', 'Metro.png')).convert()
bcgd_width = background.get_rect().width
x = 0

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
    rel_x = x % bcgd_width
    screen.blit(background, (rel_x - bcgd_width, 0))
    if rel_x < WIDTH:
        screen.blit(background, (rel_x, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
