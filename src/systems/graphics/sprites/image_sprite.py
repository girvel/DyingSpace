from math import degrees

from PIL import Image, ImageTk


class ImageSprite:
    def __init__(self, name=None, absolute_displaying=True, visible=True):
        self.visible = visible
        self.absolute_displaying = absolute_displaying

        if name:
            for format in ("gif", "png"):
                try:
                    self.sprite = Image.open(f'../assets/sprites/{name}.{format}')
                    break
                except FileNotFoundError:
                    pass
            else:
                raise FileNotFoundError
        else:
            self.sprite = None

    def display(self, canvas):
        canvas.create_image(
            self.position, self.sprite,
            rotation=0 if not hasattr(self, "rotation") else -degrees(self.rotation),
            relative=self.absolute_displaying,
        )
