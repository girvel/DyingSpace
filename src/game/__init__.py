from math import pi

from src.ecs.clocks import delta_time, Clocks
from src.ecs.union import Union
from src.game.default_data_collector import DefaultDataCollector
from src.game.ui_factory import UiFactory
from src.systems.debug import debug
from src.systems.debug.fps.fps_label import FpsLabel
from src.ecs.special_entities.named import Named
from src.systems.gameplay import gameplay
from src.systems.gameplay.cleaning.temporal import Temporal
from src.systems.gameplay.navigation.navigated import Navigated
from src.systems.gameplay.shooting.shooter import Shooter
from src.systems.graphics import graphics
from src.systems.graphics.animation import Animation
from src.systems.graphics.animation.animated import Animated
from src.systems.graphics.camera import Camera
from src.systems.graphics.deep import Deep
from src.systems.graphics.sprites.circle_sprite import CircleSprite
from src.systems.graphics.sprites.image_sprite import ImageSprite
from src.systems.graphics.sprites.line_sprite import LineSprite
from src.systems.graphics.tk_window import TkWindow
from src.systems.graphics.ui.data_container import DataContainer
from src.systems.graphics.ui.player_ui import PlayerUi
from src.systems.physics import physics
from src.systems.physics.collision.circle_collider import CircleCollider
from src.systems.physics.collision.collider import Collider
from src.systems.physics.durability.durable import Durable
from src.systems.physics.gravity.massive import Massive
from src.systems.physics.inertion.movable import Movable
from src.systems.physics.mounting.massive_system import MassiveSystem
from src.systems.physics.mounting.mounted import Mounted
from src.systems.physics.positioned import Positioned
from src.systems.physics.rotated import Rotated
from src.systems.physics.traction.tractor import Tractor
from src.tools import vector
from src.tools.vector import Vector


# Clocks

DEBUG = True

clocks = Clocks(
    DEBUG,
    physics,
    gameplay,
    graphics,
    *(() if not DEBUG else (
        debug,
    )),
)


def create(first, *components):
    e = Union(first, *components) if components else first
    clocks.register_entity(e)
    return e


# Game entities

def asteroid(name, position, radius, mass):
    return (
        Named(name),
        Positioned(position),
        CircleSprite(radius),
        Massive(mass),
        Movable(),
        Collider(resilience_k=0.3),
    )


asteroid1 = create(
    *asteroid("A001-01: snowball", Vector(0, 0), 300, 1e8),
)

create(Union(
    G=1e-3,
    g_min=1e-1,
))


# Player

player = create(
    ImageSprite("Drilling ship"),
    Positioned(Vector(500, 500)),
    Movable(),
    Massive(1e4),
    Tractor(Vector(0, -1), 1e5),
    CircleCollider(25, resilience_k=0.7),
    Animated(
        {(lambda self: self.traction_enabled): Animation("drilling_ship/movement", 1.5, 9)}
    ),
    Rotated(0),
    Navigated(asteroid1),
    Durable(1.25e8),
    DefaultDataCollector('assets/texts/ui/default_data_collector.json', 'russian'),
    MassiveSystem(),
)

gun = create(
    ImageSprite("Gauss gun"),
    Movable(),
    Massive(50),
    Mounted(player, Vector(-4, -20)),
    Rotated(0),
    Shooter(
        lambda: Union(
            CircleSprite(3),
            Collider(resilience_k=0.8),
            Massive(10),
            Durable(1e4),
            Temporal(60),
        ),
        1000,
        Vector(50, 0),
    ),
    MassiveSystem(),
)

landing_module = create(
    Massive(1),
    Movable(),
    Mounted(player, Vector(0, 25)),
    CircleCollider(10, resilience_k=-0.5),
    MassiveSystem(),
)


enemy = create(
    ImageSprite("Turret"),
    Positioned(player.position + vector.one * 300),
    Movable(),
    Massive(1e3),
    CircleCollider(13, 0.7),
    Rotated(45),
    Durable(5e7),
    MassiveSystem(),
)


# User Interface:

camera = create(
    Camera(None),
    Positioned(Vector(0, 0)),
    Deep(1),
)

display = create(
    TkWindow("Dying space", Vector(1280, 720), camera),
    PlayerUi(None),
)

display.player = player
camera.target = player

if DEBUG:
    fps_label = create(FpsLabel(display.window_root))


def traction_set(value):
    player.traction_enabled = value


def rotate(dir):
    player.rotation += dir * pi * delta_time()


def update_gun_rotation():
    gun.rotation = (display.get_mouse_position() - gun.position).angle()


def shoot():
    gun.shooting_enabled = True


display.bind_action('w', lambda e: traction_set(True))
display.bind_action('s', lambda e: traction_set(False))
display.bind_action('a', lambda e: rotate(-1))
display.bind_action('d', lambda e: rotate(1))
display.bind_action('<Motion>', lambda e: update_gun_rotation())
display.bind_action('<Button-1>', lambda e: shoot())


# speed_vector = create(
#     DataContainer(lambda: display.player.velocity ** 0 * 60, VECTOR),
#     LineSprite(None, "lightgreen", arrow_type=LAST),
#     Mounted(camera, Vector(80, 80))
# )
#
# target_vector = create(
#     DataContainer(lambda: (display.player.navigation_target.position - display.player.position) ** 0 * 60, VECTOR),
#     LineSprite(None, "red", arrow_type=LAST),
#     Mounted(camera, Vector(80, 80))
# )

ui = tuple(UiFactory(
    ui_position=Vector(20, 20),
    compass_size=100,
    blocks_offset=30,
    text_offset=20,
    font_name="Consolas 9",
).produce(display, camera))

for e in ui:
    create(e)