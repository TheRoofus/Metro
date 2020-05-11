import esper


class Position:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class MovementProcessor(esper.Processor):
    def __init__(self, minx, maxx, miny, maxy):
        super().__init__()
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def process(self):
        # This will iterate over every Entity that has BOTH of these components:
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y
            # An example of keeping the sprite inside screen boundaries. Basically,
            # adjust the position back inside screen boundaries if it tries to go outside:
            pos.x = max(self.minx, pos.x)
            pos.y = max(self.miny, pos.y)
            pos.x = min(self.maxx, pos.x)
            pos.y = min(self.maxy, pos.y)

