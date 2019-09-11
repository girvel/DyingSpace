from tkinter import LAST

from src.ecs.requirements import has, attribute


def display_info(window, holder):
    v = holder.player.velocity ** 0 * 40

    window.canvas.create_rectangle(
        50, 50,
        150, 150,
        outline='lightgreen',
    )

    window.canvas.create_line(
        100, 100,
        100 + v.x, 100 + v.y,
        fill='lightgreen',
        arrow=LAST
    )

    window.canvas.create_text(
        100, 160,
        text=f'$SPEED={round(abs(holder.player.velocity), 2)} m/s',
        fill='lightgreen',
    )


ui = (
    ("window" | has(attribute, "canvas")) * ("holder" | has(attribute, "player")) >> display_info,
)
