class RectangleSprite:
    def __init__(self, size, border):
        self.size = size
        self.color = border
        self.is_rectangle = True

    def __repr__(self):
        return "{{RectangleSprite: {0}, color={1}}}".format(
            self.size,
            self.color,
        )
