from tkinter import LAST, W

from src.ecs.requirements import has, attribute
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

    window.create_rectangle(
        UI_POSITION, DISPLAY_SIZE,
        border='lightgreen',
        relative=False,
    )

    for d in vectors:
        v = d[0] ** 0 * 40
        window.create_line(
            DISPLAY_CENTER, v,
            fill=d[1],
            arrow=LAST,
            relative=False,
        )

    p = UI_POSITION + (DISPLAY_SIZE.y + 30) * Vector.down
    for d in strings:
        window.create_text(
            p, f'${d[1].upper()}={d[0]} {d[3]}',
            fill=d[2],
            relative=False,
        )
        p += 20 * Vector.down


ui = (
    ("window" | has(attribute, "canvas")) * ("holder" | has(attribute, "player")) >> display_info,
)
