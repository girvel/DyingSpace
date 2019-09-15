class RectangleSprite:
    def __init__(self, begin, size, border, relative_displaying=True):
        self.rectangle_begin = begin
        self.rectangle_size = size
        self.border_color = border
        self.relative_displaying = relative_displaying

    def display(self, canvas):
        canvas.create_rectangle(self.rectangle_begin, self.rectangle_size, relative=self.relative_displaying, border=self.border_color)
