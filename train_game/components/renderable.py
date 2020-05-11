import esper
import pygame
from train_game.components.position import Position


class Renderable:
    def __init__(self, image, depth=0):
        self.image = image
        self.depth = depth
        self.w = image.get_width()
        self.h = image.get_height()


class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        self.window.fill(self.clear_color)
        for ent, (rend, pos) in self.world.get_components(Renderable, Position):
            self.window.blit(rend.image, (pos.x, pos.y))

        pygame.display.flip()

