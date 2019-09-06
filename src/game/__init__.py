from tkinter import PhotoImage

from src.ecs.clocks import Clocks, delta_time
from src.ecs.union import Union
from src.game import create
from src.game.fast_functions import generate_create_function, generate_where
from src.game.ui import display
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.physics import physics
from src.systems.debug.fps_monitor import fps_monitor
from src.systems.graphics import graphics
from src.systems.graphics.image_sprite import ImageSprite
from src.systems.physics.constant_holder import ConstantHolder
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
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
    ImageSprite(PhotoImage(file="../assets/sprites/drilling_ship.gif")),
    Positioned(Vector(480, 240)),
    Movable(),
    Massive(10),
)


def move_up(event):
    p.velocity += Vector(0, -10) * delta_time()


display.bind_action('w', move_up)


