from math import pi

from src.ecs.clocks import Clocks, delta_time
from src.game.default_data_collector import DefaultDataCollector
from src.game.fast_functions import generate_create_function
from src.systems.debug.fps_label import FpsLabel
from src.ecs.special_entities.named import Named
from src.systems.gameplay.navigation.navigated import Navigated
from src.systems.graphics.animation import Animation
from src.systems.graphics.animation.animated import Animated
from src.systems.graphics.camera import Camera
from src.systems.graphics.deep import Deep
from src.systems.graphics.sprites.circle_sprite import CircleSprite
from src.systems.graphics.tk_window import TkWindow
from src.systems.graphics.ui.player_ui import PlayerUi
from src.systems.physics import physics
from src.systems.debug.fps_monitor import fps_monitor
from src.systems.graphics import graphics
from src.systems.graphics.sprites.image_sprite import ImageSprite
from src.systems.physics.collision.circle_collider import CircleCollider
from src.systems.physics.constant_holder import ConstantHolder
from src.systems.physics.durability.durable import Durable
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.positioned import Positioned
from src.systems.physics.rotated import Rotated
from src.systems.physics.traction.tractor import Tractor
from src.tools.vector import Vector


DEBUG = False

# Clocks initialization

clocks = Clocks(
    graphics,
    physics,
    *(() if not DEBUG else (
        fps_monitor,
    ))
)

create = generate_create_function(clocks)


# UI

camera = create(
    Camera(None),
    Positioned(Vector(0, 0)),
    Deep(1),
)

display = create(
    TkWindow("Dying space", Vector(1024, 768), camera),
    PlayerUi(None)
)

if DEBUG:
    fps_label = create(FpsLabel(display.window_root))


# Game entities

def asteroid(name, position, radius, mass):
    return Named(name), Positioned(position), CircleSprite(radius), Massive(mass), Movable()


asteroid1 = create(
    *asteroid("A001-01: snowball", Vector(0, 0), 300, 1e8),
)

create(ConstantHolder(G=1e-3))


# Player

p = create(
    ImageSprite("drilling_ship"),
    Positioned(Vector(8000, 6000)),
    Movable(),
    Massive(1e4),
    Tractor(Vector(0, -1), 1e5),
    CircleCollider(25),
    Animated(
        {(lambda self: self.traction_enabled): Animation("drilling_ship/movement", 1.5, 9)}
    ),
    Rotated(0),
    Navigated(asteroid1),
    Durable(5e7),
    DefaultDataCollector('assets/texts/ui/default_data_collector.json', 'russian')
)

display.player = p
display.camera.target = p


def traction_set(value):
    p.traction_enabled = value


def rotate(dir):
    p.rotation += dir * pi * delta_time()


display.bind_action('w', lambda e: traction_set(True))
display.bind_action('s', lambda e: traction_set(False))
display.bind_action('a', lambda e: rotate(-1))
display.bind_action('d', lambda e: rotate(1))
