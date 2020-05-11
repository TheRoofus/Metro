import pygame
import esper

from train_game.components.position import Position, Velocity, MovementProcessor
from train_game.components.renderable import Renderable, RenderProcessor
from os import path


RESOLUTION = (800, 600)
IMAGE_DIR = path.join(path.dirname(__file__), 'resources/assets')
FPS = 60


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('My Game')
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.running = False
        self.world = esper.World()

    def __process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Here is a way to directly access a specific Entity's
                    # Velocity Component's attribute (y) without making a
                    # temporary variable.
                    self.world.component_for_entity(self.player, Velocity).x = -3
                elif event.key == pygame.K_RIGHT:
                    # For clarity, here is an alternate way in which a
                    # temporary variable is created and modified. The previous
                    # way above is recommended instead.
                    player_velocity_component = self.world.component_for_entity(self.player, Velocity)
                    player_velocity_component.x = 3
                elif event.key == pygame.K_UP:
                    self.world.component_for_entity(self.player, Velocity).y = -3
                elif event.key == pygame.K_DOWN:
                    self.world.component_for_entity(self.player, Velocity).y = 3
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.world.component_for_entity(self.player, Velocity).x = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.world.component_for_entity(self.player, Velocity).y = 0

    def __create_level(self):
        self.player = self.world.create_entity()
        self.world.add_component(self.player, Velocity(x=0, y=0))
        self.world.add_component(self.player, Renderable(image=pygame.image.load(path.join(IMAGE_DIR, "redsquare.png"))))
        self.world.add_component(self.player, Position(100, 100))

    def exec(self):

        import os
        print(os.path.dirname(os.path.abspath(__file__)))

        # Create some Processor instances, and asign them to be processed.
        render_processor = RenderProcessor(window=self.screen)
        movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])
        self.world.add_processor(render_processor)
        self.world.add_processor(movement_processor)

        self.__create_level()

        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.__process_input()
            self.world.process()

            clock.tick(FPS)

        pygame.quit()
