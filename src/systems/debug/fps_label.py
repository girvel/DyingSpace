from tkinter import Label

from src.ecs.clocks import delta_time


class FpsLabel:
    def __repr__(self):
        return '{FpsLabel}'

    @staticmethod
    def union_init(union):
        union.fps_label = Label(union.window_root)
        union.fps_label.place(x=0, y=0)

    def update_fps(self):
        self.fps_label.configure(text=str(round(1 / delta_time(), 2)))
