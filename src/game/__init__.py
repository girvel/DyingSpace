from math import pi

from src.ecs.clocks import Clocks, delta_time
from src.game.fast_functions import generate_create_function
from src.systems.debug.fps_label import FpsLabel
from src.systems.graphics.animation import Animation
from src.systems.graphics.animation.animated import Animated
from src.systems.graphics.circle_sprite import CircleSprite
from src.systems.graphics.tk_window import TkWindow
from src.systems.graphics.ui.player_ui import PlayerUi
from src.systems.physics import physics
from src.systems.debug.fps_monitor import fps_monitor
from src.systems.graphics import graphics
from src.systems.graphics.image_sprite import ImageSprite
from src.systems.physics.collision.circle_collider import CircleCollider
from src.systems.physics.constant_holder import ConstantHolder
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
from src.systems.physics.rotated import Rotated
from src.systems.physics.traction.tractor import Tractor
from src.tools.vector import Vector


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


# UI

display = create(
    TkWindow("Dying space", Vector(1024, 768)),
    PlayerUi(None),
    *(() if not __debug__ else (
        FpsLabel(),
    ))
)


# Game entities

planet = (
    CircleSprite(300),
    Positioned(Vector(320, 240)),
    Movable(),
    Massive(1e8),
)

create(ConstantHolder(G=1e-3))

create(*planet)


# Player

p = create(
    ImageSprite("drilling_ship"),
    Positioned(Vector(480, 700)),
    Movable(),
    Massive(1e4),
    Tractor(Vector(0, -1), 1e5),
    CircleCollider(25),
    Animated(
        {(lambda self: self.traction_enabled): Animation("drilling_ship/movement", 1.5)}
    ),
    Rotated(0),
)

display.player = p
display.camera_target = p


def traction_set(value):
    p.traction_enabled = value


def rotate(dir):
    p.rotation += dir * pi * delta_time()


display.bind_action('w', lambda e: traction_set(True))
display.bind_action('s', lambda e: traction_set(False))
display.bind_action('a', lambda e: rotate(-1))
display.bind_action('d', lambda e: rotate(1))


