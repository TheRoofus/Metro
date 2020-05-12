import esper
import pygame
from train_game.components.position import Position
from train_game.components.rotation import Rotation
from train_game.drawable.drawable import Drawable


class Renderable:
    def __init__(self, drawable: Drawable, depth=0):
        self.drawable = drawable
        self.depth = depth


class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        self.window.fill(self.clear_color)
        for ent, (rend, pos) in self.world.get_components(Renderable, Position):
            if self.world.has_component(ent, Rotation):
                angle = self.world.component_for_entity(ent, Rotation).a
            else:
                angle = 0.0
            rend.drawable.draw(self.window, pos, angle)

        pygame.display.flip()
