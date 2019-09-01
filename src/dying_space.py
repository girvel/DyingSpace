from src.ecs.clocks import Clocks
from src.ecs.union import Union
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.graphics.graphics import graphics
from src.systems.graphics.tk_window import TkWindow
from src.systems.physics.inertion.inertia import inertia
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
from src.systems.physics.vector import Vector

clocks = Clocks(
    graphics,
    inertia,
)


def create(*components):
    e = Union(*components)
    clocks.register_entity(e)
    return e


create(TkWindow("Dying space", 640, 480))
create(
    CircleSprite(50),
    Positioned(Vector(320, 240)),
    Movable(Vector(35, 10))
)

if __name__ == '__main__':
    clocks.mainloop()
