from _tkinter import TclError

from src.ecs.clocks import Clocks
from src.ecs.requirements import has, method, attribute

displayable = ("displayable" | has(method, "display"))
display = ("display" | has(attribute, "canvas"))


def clear(display):
    display.canvas.delete("all")


def put(displayable, display):
    displayable.display(display.canvas)


def update(display):
    display.canvas.update()
    try:
        display.canvas.update_idletasks()
    except TclError:
        raise Clocks.EndGameError


graphics = (
    display               >> clear,
    displayable * display >> put,
    display               >> update,
)
