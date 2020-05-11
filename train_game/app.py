import pygame
import esper
import pymunk
import train_game.components.physics

from train_game.components.position import Position
from train_game.components.physics import Physics, PhysicsProcessor
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
        self.phys_world = pymunk.Space()
        self.phys_world.gravity = 0.0, 0.0

    def __process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.world.component_for_entity(self.player, Physics). \
                        body.apply_impulse_at_local_point((-100, 0))
                elif event.key == pygame.K_RIGHT:
                    self.world.component_for_entity(self.player, Physics). \
                        body.apply_impulse_at_local_point((100, 0))
                elif event.key == pygame.K_UP:
                    self.world.component_for_entity(self.player, Physics).body.apply_impulse_at_local_point((0, -100))
                elif event.key == pygame.K_DOWN:
                    self.world.component_for_entity(self.player, Physics).body.apply_impulse_at_local_point((0, 100))
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def __create_level(self):
        self.player = self.world.create_entity()
        self.world.add_component(self.player,
                                 Physics(self.phys_world, shape_data=[50],
                                         body_shape_type=train_game.components.physics.BodyShapeType.BOX,
                                         body_type=train_game.components.physics.BodyType.DYNAMIC))
        self.world.add_component(self.player, Position(100, 100))
        self.world.add_component(self.player,
                                 Renderable(image=pygame.image.load(path.join(IMAGE_DIR, "redsquare.png"))))

        wall = self.world.create_entity()
        self.world.add_component(
            wall,
            Physics(self.phys_world,
                    body_type=train_game.components.physics.BodyType.STATIC,
                    body_shape_type=train_game.components.physics.BodyShapeType.SEGMENT,
                    shape_data=[(0, 0), (RESOLUTION[0], 0)])
        )
        self.world.add_component(wall, Position(0, 0))

        wall = self.world.create_entity()
        self.world.add_component(
            wall,
            Physics(self.phys_world,
                    body_type=train_game.components.physics.BodyType.STATIC,
                    body_shape_type=train_game.components.physics.BodyShapeType.SEGMENT,
                    shape_data=[(RESOLUTION[0], 0), (RESOLUTION[0], RESOLUTION[1])])
        )
        self.world.add_component(wall, Position(0, 0))

        wall = self.world.create_entity()
        self.world.add_component(wall, Position(0, 0))
        self.world.add_component(
            wall,
            Physics(self.phys_world,
                    body_type=train_game.components.physics.BodyType.STATIC,
                    body_shape_type=train_game.components.physics.BodyShapeType.SEGMENT,
                    shape_data=[(RESOLUTION[0], RESOLUTION[1]), (0, RESOLUTION[1])])
        )

        wall = self.world.create_entity()
        self.world.add_component(
            wall,
            Physics(self.phys_world,
                    body_type=train_game.components.physics.BodyType.STATIC,
                    body_shape_type=train_game.components.physics.BodyShapeType.SEGMENT,
                    shape_data=[(0, RESOLUTION[1]), (0, 0)])
        )
        self.world.add_component(wall, Position(0, 0))

    def exec(self):
        render_processor = RenderProcessor(window=self.screen)
        movement_processor = PhysicsProcessor(self.phys_world)
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
