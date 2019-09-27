class RectangleSprite:
    def __init__(self, begin, size, border):
        self.rectangle_begin = begin
        self.rectangle_size = size
        self.border_color = border

    def __repr__(self):
        return "{{RectangleSprite: {0} + {1}, color={2}}}".format(
            self.rectangle_begin,
            self.rectangle_size,
            self.border_color,
        )
