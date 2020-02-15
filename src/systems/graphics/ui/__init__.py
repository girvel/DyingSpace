from tkinter import LAST, W

from src.ecs.requirements.has import has
from src.ecs.union import Union
from src.systems.graphics.sprites.line_sprite import LineSprite
from src.systems.graphics.sprites.rectangle_sprite import RectangleSprite
from src.systems.graphics.sprites.text_sprite import TextSprite
from src.systems.graphics.ui_element import UiElement
from src.systems.physics.positioned import Positioned
from src.tools.vector import Vector


def display_info(window, holder):
    UI_POSITION = Vector(20, 20)
    DISPLAY_SIZE = Vector(100, 100)
    DISPLAY_CENTER = UI_POSITION + DISPLAY_SIZE / 2

    player = holder.player

    combined_data = player.get_combined_data()

    vectors = tuple(
        (data[0], data[2]) for data in combined_data
    )

    numerics = tuple(
        (abs(data[0]), ) + data[1:] for data in combined_data
    ) + player.get_numeric_data()

    strings = player.get_string_data() + tuple(
        (str(round(d[0], 2)), ) + d[1:] for d in numerics
    )

    rect = Union(
        Positioned(UI_POSITION),
        RectangleSprite(DISPLAY_SIZE, 'lightgreen'),
        UiElement()
    )

    vectors_unions = [
        Union(
            Positioned(DISPLAY_CENTER),
            LineSprite(d[0] ** 0 * 40, d[1], LAST),
            UiElement()
        )
        for d in vectors
    ]

    p = UI_POSITION + (DISPLAY_SIZE.y + 30) * Vector.down
    strings_unions = [
        Union(
            Positioned(p + i * 20 * Vector.down),
            TextSprite(f'${d[1].upper()}={d[0]} {d[3]}', "Consolas 10", d[2]),
            UiElement()
        )
        for i, d in enumerate(strings)
    ]

    for d in strings_unions + vectors_unions + [rect]:
        window.put(d)


ui = (
    ("window" | has("canvas")) * ("holder" | has("player")) >> display_info,
)
