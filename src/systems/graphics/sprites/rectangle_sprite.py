class RectangleSprite:
    def __init__(self, begin, size, border, absolute_displaying=True):
        self.rectangle_begin = begin
        self.rectangle_size = size
        self.border_color = border
        self.absolute_displaying = absolute_displaying

    def display(self, canvas):
        canvas.create_rectangle(
            self.rectangle_begin,
            self.rectangle_size,
            relative=self.absolute_displaying,
            border=self.border_color)
