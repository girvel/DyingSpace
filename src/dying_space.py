from tkinter import PhotoImage

from src.ecs.clocks import Clocks, delta_time
from src.ecs.union import Union
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.graphics.graphics import graphics
from src.systems.graphics.image_sprite import ImageSprite
from src.systems.graphics.tk_window import TkWindow
from src.systems.physics.collision.collision import collision
from src.systems.physics.constant_holder import ConstantHolder
from src.systems.physics.gravity.gravity import gravity
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.inertia import inertia
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
from src.systems.physics.vector import Vector

clocks = Clocks(
    graphics,
    inertia,
    gravity,
    collision,
)


def create(*components):
    e = Union(*components)
    clocks.register_entity(e)
    return e


def _where(self, **kw):
    for key, value in kw.items():
        setattr(self, key, value)
    return self


Union.where = _where

ball = (
    CircleSprite(50),
    Positioned(Vector(320, 240)),
    Movable(),
    Massive(10),
)

display = create(TkWindow("Dying space", 640, 480))

create(*ball)
p = create(
    ImageSprite(PhotoImage(file="../assets/sprites/drilling_ship.gif")),
    Positioned(Vector(480, 240)),
    Movable(),
    Massive(10),
)


def move_up(event):
    p.velocity += Vector(0, -10) * delta_time()


display.bind_action('w', move_up)

create(ConstantHolder(G=1000))


if __name__ == '__main__':
    clocks.mainloop()
