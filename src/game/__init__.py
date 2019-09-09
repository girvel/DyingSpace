from src.ecs.clocks import Clocks
from src.ecs.union import Union
from src.game.fast_functions import generate_create_function, generate_where
from src.systems.debug.fps_label import FpsLabel
from src.systems.graphics.animation import Animation
from src.systems.graphics.animation.animated import Animated
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.graphics.tk_window import TkWindow
from src.systems.physics import physics
from src.systems.debug.fps_monitor import fps_monitor
from src.systems.graphics import graphics
from src.systems.graphics.image_sprite import ImageSprite
from src.systems.physics.constant_holder import ConstantHolder
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
from src.systems.physics.traction.tractor import Tractor
from src.systems.physics.vector import Vector


# Clocks initialization

clocks = Clocks(
    graphics,
    physics,
    *(() if not __debug__ else (
        fps_monitor,
    ))
)


# Fast methods

create = generate_create_function(clocks)
generate_where(Union)


# UI

display = create(
    TkWindow("Dying space", 640, 1080),
    *(() if not __debug__ else (
        FpsLabel(),
    ))
)


# Game entities

ball = (
    CircleSprite(50),
    Positioned(Vector(320, 240)),
    Movable(),
    Massive(10),
)

create(ConstantHolder(G=1000))

create(*ball)


# Player

p = create(
    ImageSprite("drilling_ship"),
    Positioned(Vector(480, 1000)),
    Movable(),
    Massive(10),
    Tractor(Vector(0, -1), 500),
    Animated(
        {(lambda self: self.traction_enabled): Animation("drilling_ship/movement", 3)}
    )
)


def move_up(event):
    p.traction_enabled ^= True


display.bind_action('w', move_up)


