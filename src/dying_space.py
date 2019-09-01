from src.ecs.clocks import Clocks
from src.ecs.union import Union
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.graphics.graphics import graphics
from src.systems.graphics.tk_window import TkWindow
from src.systems.placing.positioned import Positioned
from src.systems.placing.vector import Vector

clocks = Clocks(
    graphics,
)


def create(*components):
    e = Union(*components)
    clocks.register_entity(e)
    return e


create(TkWindow("Dying space", 200, 200))
create(CircleSprite(10), Positioned(Vector(100, 100)))

if __name__ == '__main__':
    clocks.mainloop()
