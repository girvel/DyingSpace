from tkinter import Label

from src.ecs.clocks import Clocks


class FpsLabel:
    def __init__(self, master):
        self.fps_label = Label(master)
        self.fps_label.place(x=0, y=0)

    def __repr__(self):
        return '{FpsLabel}'

    def update_fps(self):
        self.fps_label.configure(text=str(round(Clocks.current_ups, 2)))
