from math import degrees

from PIL import Image, ImageTk


class ImageSprite:
    def __init__(self, name=None):
        self.sprite = Image.open(f'../assets/sprites/{name}.gif') if name else None
        self.tkinter_sprite = ImageTk.PhotoImage(self.sprite)

    def display(self, canvas, d):
        self.tkinter_sprite = ImageTk.PhotoImage(
            self.sprite.rotate(
                0 if not hasattr(self, "rotation") else -degrees(self.rotation),
                expand=True,
            )
        )

        p = self.position - d
        canvas.create_image(
            p.x, p.y,
            image=self.tkinter_sprite,
        )
