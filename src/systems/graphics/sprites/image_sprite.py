from PIL import Image, ImageTk


class ImageSprite:
    def __init__(self, name=None, visible=True):
        self.visible = visible

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
