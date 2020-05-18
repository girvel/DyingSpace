from tkinter import LAST

from src.ecs.union import Union
from src.systems.graphics.sprites.line_sprite import LineSprite
from src.systems.graphics.sprites.rectangle_sprite import RectangleSprite
from src.systems.graphics.sprites.text_sprite import TextSprite
from src.systems.graphics.ui import data_types
from src.systems.graphics.ui.data_container import DataContainer
from src.systems.graphics.ui_element import UiElement
from src.systems.physics.mounting.mounted import Mounted
from src.systems.physics.positioned import Positioned
from src.tools import vector


class UiFactory:
    def __init__(self, ui_position, compass_size, blocks_offset, text_offset, font_name):
        self.ui_position = ui_position
        self.compass_size = compass_size
        self.blocks_offset = blocks_offset
        self.text_offset = text_offset
        self.font_name = font_name

    def produce(self, holder, camera):
        display_center = self.ui_position + self.compass_size / 2 * vector.one

        combined_data = holder.player.get_vector_data()

        vectors = tuple(
            (data[1], data[2]) for data in combined_data
        )

        scalars = tuple(
            (
                t[0],
                (lambda tt:
                 lambda: abs(tt[1]())
                 )(t),
                t[2]
            ) for t in combined_data
        ) + holder.player.get_scalar_data()

        strings = tuple(
            (
                (lambda tt:
                 lambda: tt[0].format(round(tt[1](), 2))
                 )(t),
                t[2]
            ) for t in scalars
        ) + holder.player.get_string_data()

        yield Union(
            Mounted(camera, self.ui_position),
            RectangleSprite(self.compass_size * vector.one, 'lightgreen')
        )

        for d in vectors:
            yield Union(
                Mounted(camera, display_center),
                DataContainer((lambda prev: lambda: prev() ** 0 * (self.compass_size / 2 - 1))(d[0]), data_types.vector),
                LineSprite(None, d[1], LAST),
            )

        p = self.ui_position + (self.compass_size + self.blocks_offset) * vector.down
        for i, t in enumerate(strings):
            yield Union(
                Mounted(camera, p + i * self.text_offset * vector.down),
                DataContainer(t[0], data_types.text),
                TextSprite(None, self.font_name, t[1]),
            )
