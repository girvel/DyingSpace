from src.ecs.clocks import Clocks
from src.ecs.union import Union
from src.systems.debug import debug
from src.systems.gameplay import gameplay
from src.systems.graphics import graphics
from src.systems.physics import physics


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


def create(*components):
    e = Union(*components)
    clocks.register_entity(e)
    return e
