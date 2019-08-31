from tkinter import Tk, Canvas, BOTH

from src.ecs.requirements import has, method, attribute


class Graphics:
    requirements = ("displayable" | has(method, "display") & has(method, "d")) \
                   * ("displayer" | has(attribute, "canvas"))

    def __init__(self):
        self.subjects = []

        root = Tk()
        root.geometry("640x480")
        root.title("Dying space")

        self.canvas = Canvas(root)
        self.canvas.pack(fill=BOTH, expand=1)

    @staticmethod
    def update(displayable, displayer):
        displayable.display(displayer.canvas)
