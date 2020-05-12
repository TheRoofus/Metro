import esper
import pymunk

from enum import Enum
from pymunk.vec2d import Vec2d
from train_game.components.position import Position
from train_game.components.rotation import Rotation


class BodyShapeType(Enum):
    CIRCLE = 1
    BOX = 2
    POLYGON = 3
    SEGMENT = 4


class BodyType(Enum):
    STATIC = 1
    DYNAMIC = 2
    KINETIC = 3


class Physics:
    def __init__(self, phys_world, mass=1.0, x=0.0, y=0.0, body_type=BodyType.DYNAMIC,
                 body_shape_type=BodyShapeType.CIRCLE, shape_data=[1.0]):
        if body_shape_type == BodyShapeType.CIRCLE:
            moment = pymunk.moment_for_circle(mass, 0, shape_data[0])
            self.body = pymunk.Body(mass, moment)
            self.shape = pymunk.Circle(self.body, shape_data[0])
        elif body_shape_type == BodyShapeType.BOX:
            size = shape_data[0]
            moment = pymunk.moment_for_box(mass, (size, size))
            size = size * 0.5
            self.body = pymunk.Body(mass, moment)
            self.shape = pymunk.Poly(self.body, [(-size, size), (size, size), (size, -size), (-size, -size)])
        elif body_shape_type == BodyShapeType.SEGMENT:
            moment = pymunk.moment_for_segment(mass, shape_data[0], shape_data[1], 1)
            self.body = pymunk.Body(mass, moment)
            self.shape = pymunk.Segment(phys_world.static_body, shape_data[0], shape_data[1], 1)
        else:
            moment = pymunk.moment_for_poly(mass, shape_data)
            self.body = pymunk.Body(mass, moment)
            self.shape = pymunk.Circle(self.body, shape_data[0])

        if body_type == BodyType.DYNAMIC:
            self.body.body_type = pymunk.Body.DYNAMIC
        elif body_type == BodyType.STATIC:
            self.body.body_type = pymunk.Body.STATIC
        else:
            self.body.body_type = pymunk.Body.KINEMATIC

        self.shape.elasticity = 0.5
        self.shape.friction = 1
        self.body.position = (x, y)
        self.body.start_position = Vec2d(self.body.position)

        phys_world.add(self.body, self.shape)


class PhysicsProcessor(esper.Processor):
    def __init__(self, phys_world):
        super().__init__()
        self.phys_world = phys_world

    def process(self):
        # TODO: Нужно брать это число из настроек всей игры
        self.phys_world.step(0.01)

        for ent, (phys, pos) in self.world.get_components(Physics, Position):
            pos.x = phys.body.position.x
            pos.y = phys.body.position.y

            if self.world.has_component(ent, Rotation):
                self.world.component_for_entity(ent, Rotation).a = phys.body.angle

