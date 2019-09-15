from tkinter import LAST, W

from src.ecs.requirements import has, attribute
from src.tools.vector import Vector


def distance_vector(from_, to):
    result = to.position - from_.position

    if hasattr(from_, "radius"):
        result *= (1 - from_.radius / abs(result))

    if hasattr(to, "radius"):
        result *= (1 - to.radius / abs(result))

    return result


def display_info(window, holder):
    UI_POSITION = Vector(20, 20)
    DISPLAY_SIZE = Vector(100, 100)
    DISPLAY_CENTER = UI_POSITION + DISPLAY_SIZE / 2

    combined_data = (
        (holder.player.velocity / 1000, "speed", "lightgreen", "km/s"),
        (distance_vector(holder.player, holder.player.navigation_target) / 1000, "distance_to_target", "red", "km"),
    )

    integer_data = (
        (holder.player.mass / 1000, "mass", "green", "tn"),
        (holder.player.traction_force / 1000, "traction_force", "green", "kN"),
        (holder.player.durability, "durability", "green", "")
    )

    vectors = tuple(
        (data[0], data[2]) for data in combined_data
    )

    integers = tuple(
        (abs(data[0]), ) + data[1:] for data in combined_data
    ) + integer_data

    window.canvas.create_rectangle(
        UI_POSITION.x, UI_POSITION.y,
        UI_POSITION.x + DISPLAY_SIZE.x, UI_POSITION.y + DISPLAY_SIZE.y,
        outline='lightgreen',
    )

    for d in vectors:
        v = d[0] ** 0 * 40
        window.canvas.create_line(
            DISPLAY_CENTER.x,       DISPLAY_CENTER.y,
            DISPLAY_CENTER.x + v.x, DISPLAY_CENTER.y + v.y,
            fill=d[1],
            arrow=LAST,
        )

    y = UI_POSITION.y + DISPLAY_SIZE.y + 30
    for d in integers:
        window.canvas.create_text(
            UI_POSITION.x, y,
            text=f'${d[1].upper()}={round(d[0], 2)} {d[3]}',
            fill=d[2],
            anchor=W,
            font="Consolas 10"
        )
        y += 20


ui = (
    ("window" | has(attribute, "canvas")) * ("holder" | has(attribute, "player")) >> display_info,
)
