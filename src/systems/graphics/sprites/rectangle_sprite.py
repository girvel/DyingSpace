class RectangleSprite:
    def __init__(self, size, border):
        self.size = size
        self.color = border
        self.sprite_type = "rectangle"
        self.display_radius = abs(self.size)

    def __repr__(self):
        return "{{RectangleSprite: {0}, color={1}}}".format(
            self.size,
            self.color,
        )
