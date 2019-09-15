from math import degrees

from PIL import Image, ImageTk


class ImageSprite:
    def __init__(self, name=None, relative_displaying=True):
        self.relative_displaying = relative_displaying
        self.sprite = Image.open(f'../assets/sprites/{name}.gif') if name else None
        self.tkinter_sprite = ImageTk.PhotoImage(self.sprite)

    def display(self, canvas):
        canvas.create_image(
            self.position, self.sprite,
            rotation=0 if not hasattr(self, "rotation") else -degrees(self.rotation),
            relative=self.relative_displaying,
        )
