import os
from math import floor
from tkinter import PhotoImage

from src.ecs.clocks import delta_time
from src.ecs.requirements import attribute, has
from src.tools.limited import Limited


class Animation:
    PATH = '../assets/animations'

    def __init__(self, name, length):
        self.sprites = [
            PhotoImage(file=f'{self.PATH}/{name}/{p}')
            for p in sorted(os.listdir(f'{self.PATH}/{name}')) if p.endswith(".gif")
        ]
        self.time = Limited(0, max_value=length, min_value=0)


def animate(animated):
    for condition, animation_ in animated._Animated__dict.items():
        animation_.time.step((1 if condition(animated) else -1) * delta_time())
        animated.sprite = animation_.sprites[
            min(
                floor((animation_.time.to_proportion()) * len(animation_.sprites)),
                len(animation_.sprites) - 1
            )
        ]


animation = (
    ("animated" | has(attribute, "_Animated__dict") & has(attribute, "sprite")) >> animate,
)
