from PIL import Image, ImageTk


class ImageSprite:
    def __init__(self, name=None, visible=True):
        self.visible = visible

        if name:
            for format in ("gif", "png"):
                try:
                    self.sprite = Image.open(f'assets/sprites/{name}.{format}')
                    break
                except FileNotFoundError:
                    pass
            else:
                raise FileNotFoundError
        else:
            self.sprite = None

        self.sprite_name = name
        self.sprite_type = "image"
        self.display_radius = max(*self.sprite.size) if self.sprite else 0

    def __repr__(self):
        return "{{ImageSprite: '{0}'{1}}}".format(
            self.sprite_name,
            "" if self.visible else ", invisible"
        )
