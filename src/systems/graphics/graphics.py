from _tkinter import TclError

from src.ecs.clocks import Clocks
from src.ecs.requirements import has, method, attribute

displayable = ("displayable" | has(method, "display"))
display = ("display" | has(attribute, "canvas"))


def pre_update(display):
    display.canvas.delete("all")


def update(displayable, display):
    displayable.display(display.canvas)


def post_update(display):
    display.canvas.update()
    try:
        display.canvas.update_idletasks()
    except TclError:
        raise Clocks.EndGameError


graphics = (
    display >> pre_update,
    displayable * display >> update,
    display >> post_update,
)
