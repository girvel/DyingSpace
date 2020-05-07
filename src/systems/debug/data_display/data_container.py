from tkinter import LAST

from src.systems.graphics.sprites.line_sprite import LineSprite
from src.systems.physics.positioned import Positioned
from src.tools.vector import Vector


class DataContainer:
    def __init__(self, subject, func):
        self.debug_func = func
        self.debug_subject = subject


def debug_container(color, entity, func):
    return (
        Positioned(Vector.zero),
        LineSprite(Vector.zero, color, LAST),
        DataContainer(entity, func),
    )
