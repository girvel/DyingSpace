from _tkinter import TclError

from src.ecs.clocks import Clocks
from src.ecs.requirements import has, method, attribute
from src.systems.graphics.animation import animation
from src.systems.graphics.ui import ui

displayable = ("displayable" | has(method, "display"))
display = ("display" | has(attribute, "canvas"))


def clear(display):
    display.canvas.delete("all")
    display.camera_position = display.camera_target.position - display.size / 2


def put(displayable, display):
    displayable.display(display.canvas, display.camera_position)


def update(display):
    display.canvas.update()
    try:
        display.canvas.update_idletasks()
    except TclError:
        raise Clocks.EndGameError


graphics = (
    *animation,
    display               >> clear,
    displayable * display >> put,
    *ui,
    display               >> update,
)
