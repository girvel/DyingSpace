from tkinter import Label

from src.ecs.clocks import delta_time


class FpsLabel:
    @staticmethod
    def union_init(union):
        union.fps_label = Label(union._TkWindow__root)
        union.fps_label.place(x=0, y=0)

    def update_fps(self):
        self.fps_label.configure(text=str(round(1 / delta_time(), 2)))
