import pygame
from Media.colors import colors
from Logic.men.testPlayer import Player
import os

"""
Создание основных окон и запуск модулей для последующего 
выполнения в приложении.
"""

WIDTH = 800
HEIGHT = 600
FPS = 30

# class Window(object):
#     """
#     Создание таких окон как Меню (menu),
#     основного окна отображения игры (general),
#     окно с настройками (settings),
#     создание и редактирование карты (maps_creator)
#     """
#     def __init__(self, menu, general, settings, maps_creators):
#         self.menu = menu
#         self.general = general
#         self.settings = settings
#         self.maps = maps_creators

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(Player())

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
    screen.fill(colors.blue)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

