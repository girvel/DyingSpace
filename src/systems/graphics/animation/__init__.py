import os
from math import floor

from PIL import Image

from src.ecs.clocks import delta_time
from src.ecs.requirements import attribute, has
from src.tools.limited import Limited


class Animation:
    PATH = 'assets/animations'

    def __init__(self, name, length, ending_loop_index=None):
        self.sprites = [
            Image.open(f'{self.PATH}/{name}/{p}')
            for p in sorted(os.listdir(f'{self.PATH}/{name}'), key=lambda s: int(s[:-4])) if p.endswith(".png")
        ]

        self.ending_loop_starts = \
            ending_loop_index / len(self.sprites) * length \
            if ending_loop_index else len(self.sprites)

        self.time = Limited(0, max_value=length, min_value=0)


def animate(animated):
    for condition, animation_ in animated._Animated__dict.items():
        if condition(animated):
            if animation_.time.value >= animation_.ending_loop_starts:
                animation_.time.min_value = animation_.ending_loop_starts
                animation_.time.cycled_step(delta_time())
                animation_.time.min_value = 0
            else:
                animation_.time.step(delta_time())
        else:
            animation_.time.min_value = 0
            animation_.time.step(-delta_time())

        animated.sprite = animation_.sprites[
            min(
                floor((animation_.time.to_proportion()) * len(animation_.sprites)),
                len(animation_.sprites) - 1
            )
        ]


animation = (
    ("animated" | has(attribute, "_Animated__dict") & has(attribute, "sprite")) >> animate,
)
