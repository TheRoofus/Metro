import pygame
import sys

"""
Создание основных окон и запуск модулей для последующего 
выполнения в приложении.
"""

class Window(object):
    """
    Создание таких окон как Меню (menu),
    основного окна отображения игры (general),
    окно с настройками (settings),
    создание и редактирование карты (maps_creator)
    """
    def __init__(self, menu, general, settings, maps_creators):
        self.menu = menu
        self.general = general
        self.settings = settings
        self.maps = maps_creators