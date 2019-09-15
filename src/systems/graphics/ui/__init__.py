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
    for d in integers:
        window.create_text(
            p, f'${d[1].upper()}={round(d[0], 2)} {d[3]}',
            fill=d[2],
            relative=False,
        )
        p += 20 * Vector.down


ui = (
    ("window" | has(attribute, "canvas")) * ("holder" | has(attribute, "player")) >> display_info,
)
